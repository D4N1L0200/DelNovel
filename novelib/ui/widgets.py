from abc import ABC, abstractmethod
from .layout import Anchor, Sizing, Order

# from .interactions import Action # TODO: Fix circular import
from typing import TypeVar, Optional
import pygame as pg

T = TypeVar("T", bound="Widget")


class Widget(ABC):
    def __init__(
        self, anchor: Anchor, sizing: Sizing, order: Order = Order.VERTICAL
    ) -> None:
        self.anchor: Anchor = anchor
        self.sizing: Sizing = sizing
        self.order: Order = order
        self.widgets: list[Widget] = []

    def addWidget(self, widget: T) -> None:
        self.widgets.append(widget)

    def calcSize(
        self, size: tuple[int, int]
    ) -> tuple[list[tuple[int, int]], tuple[int, int]]:
        offsets: list[tuple[int, int]] = []

        match self.sizing:
            case Sizing.FILL:
                pass
            case Sizing.COVER:
                size = (0, 0)

                match self.order:
                    case Order.VERTICAL:
                        for widget in self.widgets:
                            _, widg_size = widget.calcSize(size)
                            offsets.append((0, size[1]))
                            size = (max(size[0], widg_size[0]), widg_size[1])
                    case Order.HORIZONTAL:
                        for widget in self.widgets:
                            _, widg_size = widget.calcSize(size)
                            offsets.append((size[0], 0))
                            size = (widg_size[0], max(size[1], widg_size[1]))
                    case _:
                        pass  # TODO: raise
            case _:
                pass  # TODO: raise

        return offsets, size

    @abstractmethod
    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None: ...


class ClickableWidget(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing) -> None:
        super().__init__(anchor, sizing)

    @abstractmethod
    def onClick(self) -> None: ...


class WritableWidget(Widget):
    font: Optional[pg.font.Font] = None

    def __init__(self, anchor: Anchor, sizing: Sizing, text: str) -> None:
        super().__init__(anchor, sizing)
        self.text: str = text
        self.font: pg.font.Font = WritableWidget.font

    def calcSize(
        self, size: tuple[int, int]
    ) -> tuple[list[tuple[int, int]], tuple[int, int]]:
        if not self.font:
            return [], (0, 0)  # TODO: raise
        match self.sizing:
            case Sizing.FILL:
                pass
            case Sizing.COVER:
                text: pg.Surface = self.font.render(self.text, False, (0, 0, 0))
                size = (text.get_width(), text.get_height())
            case _:
                pass  # TODO: raise

        return [], size


class Background(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing, image_name: str) -> None:
        super().__init__(anchor, sizing)
        self.image_name: str = image_name

    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None:
        pass
        # window.blit(pg.image.load(self.image_name), (0, 0))


class Button(WritableWidget, ClickableWidget):
    def __init__(
        self,
        anchor: Anchor,
        sizing: Sizing,
        text: str,
        action,
        font: Optional[pg.font.Font] = None,
    ):
        # def __init__(self, anchor: Anchor, sizing: Sizing, text: str, font: pg.font.Font, action: Action):
        super().__init__(anchor, sizing, text=text)
        self.action = action
        # self.action: Action = action
        if font:
            self.font: pg.font.Font = font

    def onClick(self):
        self.action.execute()

    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None:
        pg.draw.rect(window, (255, 255, 255), (*pos, *size))
        text: pg.Surface = self.font.render(self.text, False, (255, 0, 0))
        window.blit(text, pos)


class Modal(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing, title: str):
        super().__init__(anchor, sizing)
        self.title: str = title
        self.is_visible: bool = False

    def show(self):
        self.is_visible = True

    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None:
        pass


class TextArea(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing, text: str):
        super().__init__(anchor, sizing)
        self.text: str = text

    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None:
        pass


class Block(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing, order: Order) -> None:
        super().__init__(anchor, sizing, order)

    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None:
        offsets, size = self.calcSize(size)

        match self.anchor:
            case Anchor.CENTER:
                pos = (
                    (window.get_width() // 2) - (size[0] // 2),
                    (window.get_height() // 2) - (size[1] // 2),
                )
            case _:
                pass  # TODO: raise

        pg.draw.rect(window, (255, 255, 255), (*pos, *size), 1)

        for idx, widget in enumerate(self.widgets):
            pos = (pos[0] + offsets[idx][0], pos[1] + offsets[idx][1])
            widget.draw(window, pos, size)
