import pygame as pg
from .widgets import Widget


class Scene:
    def __init__(self) -> None:
        self.widgets: list[Widget] = []

    def addWidget(self, widget: Widget) -> None:
        self.widgets.append(widget)


class SceneManager:
    scenes: dict[str, Scene] = {}
    active_scene: Scene = Scene()

    @classmethod
    def createScene(cls, scene_name: str) -> None:
        if scene_name in cls.scenes:
            return  # raise
        
    @classmethod
    def insertWidget(cls, scene_name: str, widget: Widget) -> None:
        if scene_name not in cls.scenes:
            return  # raise

        cls.scenes[scene_name].addWidget(widget)

    @classmethod
    def loadScene(cls, scene_name: str) -> None:
        if scene_name not in cls.scenes:
            return  # raise

        cls.active_scene = cls.scenes[scene_name]

    @classmethod
    def handleEvent(cls, event: pg.event.Event) -> None:
        pass

    @classmethod
    def drawScene(cls, window: pg.Surface) -> None:
        pass
