from abc import ABC, abstractmethod
from ..scene_manager import SceneManager
from .widgets import Widget, Modal
from ..chat_manager import ChatManager


class Action(ABC):
    @abstractmethod
    def execute(self) -> None: ...


class EmptyAction(Action):
    def execute(self) -> None:
        pass


class ExitAction(Action):
    def execute(self) -> None:
        raise KeyboardInterrupt


class SceneAction(Action):
    def __init__(self, scene_name: str) -> None:
        self.scene_name: str = scene_name

    def execute(self) -> None:
        SceneManager.loadScene(self.scene_name)


class ModalAction(Action):
    def __init__(self, modal_idx: int) -> None:
        self.modal_idx: int = modal_idx

    def execute(self) -> None:
        modal: Widget = SceneManager.active_scene.widgets[self.modal_idx]

        if isinstance(modal, Modal):
            modal.toggle()
        else:
            raise TypeError("Modal must be a Modal Widget")


class LoadChatAction(Action):
    def __init__(self, chat_source: str) -> None:
        self.chat_source: str = chat_source

    def execute(self) -> None:
        ChatManager.loadChat(self.chat_source)


class ResetChatAction(Action):
    def execute(self) -> None:
        ChatManager.unloadChat()


class Link:
    @staticmethod
    def toNone() -> EmptyAction:
        return EmptyAction()

    @staticmethod
    def toExit() -> ExitAction:
        return ExitAction()

    @staticmethod
    def toScene(scene_name: str) -> SceneAction:
        return SceneAction(scene_name)

    @staticmethod
    def toModal(modal_idx: int) -> ModalAction:
        return ModalAction(modal_idx)

    @staticmethod
    def toChat(chat_source: str) -> LoadChatAction:
        return LoadChatAction(chat_source)

    @staticmethod
    def toResetChat() -> ResetChatAction:
        return ResetChatAction()
