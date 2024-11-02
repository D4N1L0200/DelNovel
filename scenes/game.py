from novelib import SceneManager
from novelib.ui import widgets, Anchor, Sizing, Order, Link


def create() -> None:
    SceneManager.createScene("game_start")
    SceneManager.insertWidget(
        "game_start",
        widgets.Background(Anchor.TOPLEFT, Sizing.FILL, "assets/images/bg_menu.jpg"),
    )

    temp_items: widgets.Block = widgets.Block(
        Anchor.CENTER,
        Sizing.COVER,
        Order.VERTICAL,
    )

    temp_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "What a nice game...",
            Link.toNone(),
        )
    )
    temp_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "This crashes the game.",
            Link.toScene("crash"),
        )
    )
    temp_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Back to main menu.",
            Link.toScene("main_menu"),
        )
    )

    SceneManager.insertWidget("game_start", temp_items)
