from abc import ABC, abstractmethod
from .scene_manager import SceneManager
from .widgets import Modal


class Action(ABC):
    @abstractmethod
    def execute(self) -> None: ...


class SceneAction(Action):
    def __init__(self, scene_name: str) -> None:
        self.scene_name: str = scene_name

    def execute(self) -> None:
        SceneManager.loadScene(self.scene_name)


class ModalAction(Action):
    def __init__(self, modal: Modal) -> None:
        self.modal: Modal = modal

    def execute(self) -> None:
        self.modal.show()


class Link:
    @staticmethod
    def toScene(scene_name: str) -> SceneAction:
        return SceneAction(scene_name)

    @staticmethod
    def toModal(modal: Modal) -> ModalAction:
        return ModalAction(modal)
