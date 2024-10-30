from abc import ABC, abstractmethod
from .layout import Anchor, Sizing
from typing import TypeVar

T = TypeVar("T", bound="Widget")


class Widget:
    def __init__(self, anchor: Anchor, sizing: Sizing) -> None:
        self.anchor: Anchor = anchor
        self.sizing: Sizing = sizing
        self.widgets: list[Widget] = []

    def addWidget(self, widget: T) -> None:
        self.widgets.append(widget)


class Background(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing, image_name: str) -> None:
        super().__init__(anchor, sizing)
        self.image_name: str = image_name


class ClickableWidget(Widget, ABC):
    def __init__(self, anchor: Anchor, sizing: Sizing) -> None:
        super().__init__(anchor, sizing)

    @abstractmethod
    def onClick(self) -> None: ...


class Button(ClickableWidget):
    def __init__(self, anchor: Anchor, sizing: Sizing, text, action):
        super().__init__(anchor, sizing)
        self.text = text
        self.action = action

    def onClick(self):
        self.action.execute()


class Modal(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing, title: str):
        super().__init__(anchor, sizing)
        self.title: str = title
        self.is_visible: bool = False

    def show(self):
        self.is_visible = True


class TextArea(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing, text: str):
        super().__init__(anchor, sizing)
        self.text: str = text


class Block(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing) -> None:
        super().__init__(anchor, sizing)
