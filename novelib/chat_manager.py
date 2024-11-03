# import pygame as pg
import os
import json
from typing import TypedDict, Union
from .scene_manager import SceneManager
from .ui.widgets import Widget, ChatBox


class Path(TypedDict):
    actions: list[dict[str, str]]
    option_pool: str


class ChatManager:
    chat_box_idx: int = -1
    characters: dict[str, str] = {}
    option_pools: dict[str, list[dict[str, str]]] = {}
    paths: dict[str, Path] = {}
    curr_path: str = "start"
    curr_action: int = 0

    @classmethod
    def setChatBoxIdx(cls, idx: int) -> None:
        cls.chat_box_idx = idx

    @classmethod
    def loadChat(cls, filename: str) -> None:
        chat_dir = os.path.join(os.path.dirname(__file__), "..", "chats")
        filepath = os.path.join(chat_dir, f"{filename}.json")
        with open(filepath, "r") as f:
            data = json.load(f)

        cls.characters = data["characters"]
        cls.option_pools = data["option_pools"]
        cls.paths = data["paths"]

        cls.advance()

    @classmethod
    def unloadChat(cls) -> None:
        cls.characters = {}
        cls.option_pools = {}
        cls.paths = {}
        cls.curr_path = "start"
        cls.curr_action = 0

    @classmethod
    def sendChat(cls, text: str) -> None:
        chat_box: Union[Widget, ChatBox] = SceneManager.active_scene.widgets[
            cls.chat_box_idx
        ].widgets[0]
        if isinstance(chat_box, ChatBox):
            chat_box.setText(text)

    @classmethod
    def update(cls) -> None:
        cls.chat_box_idx = SceneManager.active_scene.chat_box_idx

        if cls.chat_box_idx == -1:
            return

    @classmethod
    def advance(cls) -> None:
        path: Path = cls.paths[cls.curr_path]
        actions: list[dict[str, str]] = path["actions"]

        if cls.curr_action < len(actions):
            action = actions[cls.curr_action]
            cls.curr_action += 1

            if action["type"] == "message":
                character = cls.characters[action["name"]]
                cls.sendChat(f"{character}: {action["text"]}")
        else:
            options: list[dict[str, str]] = cls.option_pools[path["option_pool"]]
            cls.sendChat(
                "\n".join(
                    [f"{i + 1}. {option['text']}" for i, option in enumerate(options)]
                )
            )
