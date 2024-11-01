import pygame as pg
from .ui.widgets import Widget, WritableWidget


class Scene:
    def __init__(self) -> None:
        self.widgets: list[Widget] = []

    def addWidget(self, widget: Widget) -> None:
        self.widgets.append(widget)


class SceneManager:
    scenes: dict[str, Scene] = {}
    active_scene: Scene = Scene()

    fonts: dict[str, pg.font.Font] = {}

    @classmethod
    def createFont(cls, font_name: str, font_path: str, font_size: int) -> None:
        pg.font.init()

        font: pg.font.Font = pg.font.Font("assets/fonts/" + font_path, font_size)
        cls.fonts[font_name] = font

        if not WritableWidget.font:
            WritableWidget.font = font

    @classmethod
    def getFont(cls, font_name: str) -> pg.font.Font:
        return cls.fonts[font_name]

    @classmethod
    def createScene(cls, scene_name: str) -> None:
        if scene_name in cls.scenes:
            return  # TODO: raise

        scene: Scene = Scene()
        cls.scenes[scene_name] = scene

    @classmethod
    def insertWidget(cls, scene_name: str, widget: Widget) -> None:
        if scene_name not in cls.scenes:
            return  # TODO: raise

        cls.scenes[scene_name].addWidget(widget)

    @classmethod
    def loadScene(cls, scene_name: str) -> None:
        if scene_name not in cls.scenes:
            return  # TODO: raise

        cls.active_scene = cls.scenes[scene_name]

    @classmethod
    def handleEvent(cls, event: pg.event.Event) -> None:
        pass

    @classmethod
    def drawScene(cls, window: pg.Surface) -> None:
        for widget in cls.active_scene.widgets:
            widget.draw(
                window, pos=(0, 0), size=(window.get_width(), window.get_height())
            )
