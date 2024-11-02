from novelib import SceneManager
from novelib.ui import widgets, Anchor, Sizing, Order, Link


def create() -> None:
    SceneManager.createScene("debug_menu")
    SceneManager.insertWidget(
        "debug_menu",
        widgets.Background(Anchor.TOPLEFT, Sizing.FILL, "assets/images/bg_menu.jpg"),
    )

    debug_items: widgets.Block = widgets.Block(
        Anchor.CENTER,
        Sizing.COVER,
        Order.VERTICAL,
    )

    debug_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Layout tests...",
            Link.toScene("debug_layout_anchor"),
        )
    )
    debug_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Go Back...",
            Link.toScene("main_menu"),
        )
    )

    SceneManager.insertWidget("debug_menu", debug_items)
