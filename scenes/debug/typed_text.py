from novelib import SceneManager
from novelib.ui import widgets, Anchor, Sizing, Order, Link


def create() -> None:
    SceneManager.createScene("debug_typed_text")
    SceneManager.insertWidget(
        "debug_typed_text",
        widgets.Background(Anchor.TOPLEFT, Sizing.FILL, "assets/images/bg_menu.jpg"),
    )

    text = widgets.TypedTextArea(
        Anchor.CENTER,
        Sizing.COVER,
        [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
            "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "Curabitur pretium tincidunt lacus.",
            "Nunc congue, risus at pellentesque convallis, sapien erat eleifend nulla, sit amet vestibulum nulla urna eget lorem.",
            "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.",
            "Integer feugiat scelerisque varius morbi enim nunc faucibus.",
            "Egestas purus viverra accumsan in nisl nisi scelerisque eu ultrices.",
        ],
        0.01,
    )

    button = widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "Back",
        Link.toScene("debug_menu"),
    )

    text_block: widgets.Block = widgets.Block(
        Anchor.CENTER,
        Sizing.COVER,
        Order.VERTICAL,
    )
    text_block.addWidget(text)
    text_block.addWidget(button)

    SceneManager.insertWidget("debug_typed_text", text_block)
