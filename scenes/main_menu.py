from novelib import SceneManager
from novelib.ui import widgets, Anchor, Sizing, Order, Link


def create() -> None:
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
    menu_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Debug",
            Link.toScene("debug_menu"),
        )
    )
    menu_items.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Exit",
            Link.toExit(),
        )
    )

    SceneManager.insertWidget("main_menu", menu_items)

    about_modal: widgets.Modal = widgets.Modal(
        Anchor.CENTER, Sizing.COVER, "About Page"
    )
    about_modal.addWidget(
        widgets.TextArea(
            Anchor.CENTER,
            Sizing.COVER,
            [
                "\t\t\t\tAbout DelNovel",
                "This is a project that started as a simple UI manager for pygame, but the goal is to have a full game in the future.",
                "An open world rpg that allows the player to travel between 'dimensions' that were chosen by my friends.",
                "I don't know for how long I'll keep working on it, but I hope it will be enough to satisfy at least one of my friends.",
                "I hope that you enjoy the game! - Del",
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
