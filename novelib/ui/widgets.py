from __future__ import annotations
from abc import ABC, abstractmethod
from .layout import Anchor, Sizing, Order
from typing import Optional
from ..themes import THEME
import pygame as pg

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .interactions import Action


class Widget(ABC):
    def __init__(
        self, anchor: Anchor, sizing: Sizing, order: Order = Order.VERTICAL
    ) -> None:
        self.anchor: Anchor = anchor
        self.sizing: Sizing = sizing
        self.order: Order = order
        self.widgets: list[Widget] = []
        self.rect: Optional[pg.Rect] = None

    def addWidget(self, widget: Widget) -> None:
        self.widgets.append(widget)

    def calcSize(
        self, size: tuple[int, int]
    ) -> tuple[list[tuple[int, int]], tuple[int, int]]:
        offsets: list[tuple[int, int]] = []
        out_size: tuple[int, int] = (0, 0)

        match self.sizing:
            case Sizing.FILL:
                pass
            case Sizing.COVER:
                out_size = (0, 0)

                match self.order:
                    case Order.VERTICAL:
                        for widget in self.widgets:
                            _, widg_size = widget.calcSize(size)
                            offsets.append((0, out_size[1]))
                            out_size = (max(out_size[0], widg_size[0]), widg_size[1])
                    case Order.HORIZONTAL:
                        for widget in self.widgets:
                            _, widg_size = widget.calcSize(size)
                            offsets.append((out_size[0], 0))
                            out_size = (widg_size[0], max(out_size[1], widg_size[1]))

        return offsets, out_size

    @abstractmethod
    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None: ...

    def handleEvent(self, event: pg.event.Event) -> None:
        for widget in self.widgets:
            widget.handleEvent(event)


class Background(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing, image_name: str) -> None:
        super().__init__(anchor, sizing)
        self.image_name: str = image_name

    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None:
        pass
        # window.blit(pg.image.load(self.image_name), (0, 0))


class ClickableWidget(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing) -> None:
        super().__init__(anchor, sizing)
        self.is_hovering: bool = False

    def handleEvent(self, event: pg.event.Event) -> None:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not self.rect:
                    return
                if self.rect.collidepoint(event.pos):
                    self.onClick(event.pos, event.button)
        elif event.type == pg.MOUSEMOTION:
            if not self.rect:
                return
            self.is_hovering = self.rect.collidepoint(event.pos)

    @abstractmethod
    def onClick(self, pos: tuple[int, int], mouse_button: int) -> None: ...


class WritableWidget(Widget):
    font: Optional[pg.font.Font] = None

    def __init__(self, anchor: Anchor, sizing: Sizing, text: list[str]) -> None:
        super().__init__(anchor, sizing)
        self.original_text: list[str] = text
        self.text: list[str] = []
        for line in text:
            line = line.replace("\t", "TEST")
            self.text.extend(line.split("\n"))
        self.font: Optional[pg.font.Font] = WritableWidget.font

    def calcSize(
        self, size: tuple[int, int]
    ) -> tuple[list[tuple[int, int]], tuple[int, int]]:
        if not self.font:
            return [], (0, 0)  # TODO: raise

        match self.sizing:
            case Sizing.FILL:
                pass
            case Sizing.COVER:
                max_size = size
                size = (0, 0)

                space: pg.Surface = self.font.render(" ", False, (0, 0, 0))
                char_width: int = space.get_width()

                idx: int = 0
                while idx < len(self.text):
                    line: str = self.text[idx]

                    text: pg.Surface = self.font.render(line, False, (0, 0, 0))

                    if text.get_width() < max_size[0]:
                        size = (
                            max(size[0], text.get_width()),
                            size[1] + text.get_height(),
                        )
                        idx += 1
                        continue

                    lines: list[str] = []
                    while text.get_width() > max_size[0]:
                        max_char: int = max_size[0] // char_width
                        last_space: int = line[:max_char].rfind(" ", 0, max_char)
                        cut_line = line[:last_space].strip()
                        line = line[last_space:].strip()
                        lines.append(cut_line)
                        text = self.font.render(line, False, (0, 0, 0))
                        size = (
                            max(size[0], char_width * len(cut_line)),
                            size[1] + text.get_height(),
                        )
                    lines.append(line)

                    self.text.pop(idx)
                    for idx_offset, line in enumerate(lines):
                        self.text.insert(idx + idx_offset, line)
                    idx += len(lines)
                    idx += 1

        size = (
            size[0] + THEME.TEXT_PADDING,
            size[1] + THEME.TEXT_PADDING + (len(self.text) - 1) * THEME.LINE_SPACING,
        )

        return [], size

    def handleEvent(self, event: pg.event.Event) -> None:
        super().handleEvent(event)

        if event.type == pg.VIDEORESIZE:
            self.text = []
            for line in self.original_text:
                line = line.replace("\t", "    ")
                self.text.extend(line.split("\n"))

    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None:
        if not self.font:
            return

        self.rect = pg.Rect(pos, size)
        pg.draw.rect(window, THEME.OUTLINE_COLOR, self.rect, 1)

        for idx, line in enumerate(self.text):
            text: pg.Surface = self.font.render(line, False, THEME.TEXT_COLOR)
            window.blit(
                text,
                (
                    pos[0] + THEME.TEXT_PADDING // 2,
                    pos[1]
                    + idx * (text.get_height() + THEME.LINE_SPACING)
                    + THEME.TEXT_PADDING // 2,
                ),
            )


class Button(WritableWidget, ClickableWidget):
    def __init__(
        self,
        anchor: Anchor,
        sizing: Sizing,
        text: str,
        action: Action,
    ) -> None:
        super().__init__(anchor, sizing, [text])
        self.action: Action = action

    def onClick(self, pos: tuple[int, int], mouse_button: int) -> None:
        self.action.execute()

    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None:
        if self.is_hovering:
            self.rect = pg.Rect(pos, size)
            pg.draw.rect(window, THEME.HOVER_COLOR, self.rect)

        return super().draw(window, pos, size)


class TextArea(WritableWidget):
    def __init__(self, anchor: Anchor, sizing: Sizing, text: list[str]) -> None:
        super().__init__(anchor, sizing, text)


class Modal(Widget):
    def __init__(self, anchor: Anchor, sizing: Sizing, title: str) -> None:
        super().__init__(anchor, sizing)
        self.title: str = title
        self.is_visible: bool = False

    def toggle(self) -> None:
        self.is_visible = not self.is_visible

    def draw(
        self, window: pg.Surface, pos: tuple[int, int], size: tuple[int, int]
    ) -> None:
        if not self.is_visible:
            return

        offsets, size = self.calcSize(size)

        match self.anchor:
            case Anchor.CENTER:
                pos = (
                    (window.get_width() // 2) - (size[0] // 2),
                    (window.get_height() // 2) - (size[1] // 2),
                )
            case _:
                raise NotImplementedError

        pg.draw.rect(window, THEME.BG_COLOR, (*pos, *size))
        pg.draw.rect(window, THEME.OUTLINE_COLOR, (*pos, *size), 1)

        for idx, widget in enumerate(self.widgets):
            pos = (pos[0] + offsets[idx][0], pos[1] + offsets[idx][1])
            widget.draw(window, pos, size)


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
            case Anchor.TOPLEFT:
                pos = (0, 0)
            case Anchor.TOPRIGHT:
                pos = (window.get_width() - size[0], 0)
            case Anchor.BOTTOMLEFT:
                pos = (0, window.get_height() - size[1])
            case Anchor.BOTTOMRIGHT:
                pos = (window.get_width() - size[0], window.get_height() - size[1])
            case _:
                raise NotImplementedError

        pg.draw.rect(window, (255, 255, 255), (*pos, *size), 1)

        for idx, widget in enumerate(self.widgets):
            pos = (pos[0] + offsets[idx][0], pos[1] + offsets[idx][1])
            widget.draw(window, pos, size)
