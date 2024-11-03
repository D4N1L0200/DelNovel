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
    i: int = 0

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
    def sendChat(cls, text: str) -> None:
        chat_box: Union[Widget, ChatBox] = SceneManager.active_scene.widgets[
            cls.chat_box_idx
        ].widgets[0]
        if isinstance(chat_box, ChatBox):
            chat_box.setText([text])

    @classmethod
    def update(cls) -> None:
        cls.chat_box_idx = SceneManager.active_scene.chat_box_idx

        if cls.chat_box_idx == -1:
            return

    @classmethod
    def advance(cls) -> None:
        if cls.i > 5:
            cls.i = 0

        match cls.i:
            case 0:
                cls.sendChat("Zero")
            case 1:
                cls.sendChat("One")
            case 2:
                cls.sendChat("Two")
            case 3:
                cls.sendChat("Three")
            case 4:
                cls.sendChat("Four")
            case 5:
                cls.sendChat("Five")
            case _:
                cls.i = 0

        cls.i += 1
