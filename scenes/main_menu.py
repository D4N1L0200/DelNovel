from typing import Optional
from novelib import SceneManager
from novelib.ui import widgets, Anchor, Sizing, Order, Link

SceneManager.createFont("PressStart", "PressStart2P.ttf", 24)

SceneManager.createScene("main_menu")
SceneManager.insertWidget(
    "main_menu",
    widgets.Background(Anchor.TOPLEFT, Sizing.FILL, "assets/images/bg_menu.jpg"),
)

menu_items: widgets.Block = widgets.Block(
    Anchor.CENTER,
    Sizing.COVER,
    Order.VERTICAL,
)

menu_items.addWidget(
    widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "Start Game",
        Link.toScene("game_start"),
    )
)
menu_items.addWidget(
    widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "Settings",
        Link.toScene("main_menu_settings"),
    )
)

SceneManager.insertWidget("main_menu", menu_items)

about_modal: widgets.Modal = widgets.Modal(Anchor.CENTER, Sizing.COVER, "About Page")
about_modal.addWidget(
    widgets.TextArea(
        Anchor.CENTER,
        Sizing.COVER,
        [
            "This is an about page.",
            "This is another line of the about page.",
            "This is a\nmultiline\nparagraph.",
        ],
    )
)

modal_idx: int = SceneManager.insertWidgetIdx("main_menu", about_modal)

button_about = widgets.Button(
    Anchor.NONE,
    Sizing.COVER,
    "About",
    Link.toModal(modal_idx),
)

about_block: widgets.Block = widgets.Block(
    Anchor.TOPRIGHT,
    Sizing.COVER,
    Order.HORIZONTAL,
)

about_block.addWidget(button_about)

SceneManager.insertWidget("main_menu", about_block)
