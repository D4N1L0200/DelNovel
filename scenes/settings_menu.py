from novelib import SceneManager
from novelib.ui import widgets, Anchor, Sizing, Order, Link


def create() -> None:
    SceneManager.createScene("main_menu_settings")
    SceneManager.insertWidget(
        "main_menu_settings",
        widgets.Background(Anchor.TOPLEFT, Sizing.FILL, "assets/images/bg_menu.jpg"),
    )

    set_items: widgets.Block = widgets.Block(
        Anchor.CENTER,
        Sizing.COVER,
        Order.VERTICAL,
    )

    set_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Imagine this does something...",
            Link.toNone(),
        )
    )
    set_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Imagine this also does something...",
            Link.toNone(),
        )
    )
    set_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "I'm getting tired of imagining this...",
            Link.toNone(),
        )
    )
    set_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Don't click me...",
            Link.toNone(),
        )
    )
    set_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Stop reading this...",
            Link.toNone(),
        )
    )
    set_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Go Back...",
            Link.toScene("main_menu"),
        )
    )

    SceneManager.insertWidget("main_menu_settings", set_items)
