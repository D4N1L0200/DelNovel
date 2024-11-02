from novelib import SceneManager
from novelib.ui import widgets, Anchor, Sizing, Order, Link


def create() -> None:
    SceneManager.createScene("debug_layout_anchor")
    SceneManager.insertWidget(
        "debug_layout_anchor",
        widgets.Background(Anchor.TOPLEFT, Sizing.FILL, "assets/images/bg_menu.jpg"),
    )

    # CENTER
    button = widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "CENTER",
        Link.toScene("debug_menu"),
    )
    center_block: widgets.Block = widgets.Block(
        Anchor.CENTER,
        Sizing.COVER,
        Order.VERTICAL,
    )
    center_block.addWidget(button)

    # TOP
    button = widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "TOP",
        Link.toScene("debug_menu"),
    )
    top_block: widgets.Block = widgets.Block(
        Anchor.TOP,
        Sizing.COVER,
        Order.VERTICAL,
    )
    top_block.addWidget(button)

    # BOTTOM
    button = widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "BOTTOM",
        Link.toScene("debug_menu"),
    )
    bottom_block: widgets.Block = widgets.Block(
        Anchor.BOTTOM,
        Sizing.COVER,
        Order.VERTICAL,
    )
    bottom_block.addWidget(button)

    # LEFT
    button = widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "LEFT",
        Link.toScene("debug_menu"),
    )
    left_block: widgets.Block = widgets.Block(
        Anchor.LEFT,
        Sizing.COVER,
        Order.VERTICAL,
    )
    left_block.addWidget(button)

    # RIGHT
    button = widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "RIGHT",
        Link.toScene("debug_menu"),
    )
    right_block: widgets.Block = widgets.Block(
        Anchor.RIGHT,
        Sizing.COVER,
        Order.VERTICAL,
    )
    right_block.addWidget(button)

    # TOP LEFT
    button = widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "TOP LEFT",
        Link.toScene("debug_menu"),
    )
    top_left_block: widgets.Block = widgets.Block(
        Anchor.TOPLEFT,
        Sizing.COVER,
        Order.VERTICAL,
    )
    top_left_block.addWidget(button)

    # TOP RIGHT
    button = widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "TOP RIGHT",
        Link.toScene("debug_menu"),
    )
    top_right_block: widgets.Block = widgets.Block(
        Anchor.TOPRIGHT,
        Sizing.COVER,
        Order.VERTICAL,
    )
    top_right_block.addWidget(button)

    # BOTTOM LEFT
    button = widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "BOTTOM LEFT",
        Link.toScene("debug_menu"),
    )
    bottom_left_block: widgets.Block = widgets.Block(
        Anchor.BOTTOMLEFT,
        Sizing.COVER,
        Order.VERTICAL,
    )
    bottom_left_block.addWidget(button)

    # BOTTOM RIGHT
    button = widgets.Button(
        Anchor.NONE,
        Sizing.COVER,
        "BOTTOM RIGHT",
        Link.toScene("debug_menu"),
    )
    bottom_right_block: widgets.Block = widgets.Block(
        Anchor.BOTTOMRIGHT,
        Sizing.COVER,
        Order.VERTICAL,
    )
    bottom_right_block.addWidget(button)

    SceneManager.insertWidget("debug_layout_anchor", center_block)

    SceneManager.insertWidget("debug_layout_anchor", top_block)
    SceneManager.insertWidget("debug_layout_anchor", bottom_block)
    SceneManager.insertWidget("debug_layout_anchor", left_block)
    SceneManager.insertWidget("debug_layout_anchor", right_block)

    SceneManager.insertWidget("debug_layout_anchor", top_left_block)
    SceneManager.insertWidget("debug_layout_anchor", top_right_block)
    SceneManager.insertWidget("debug_layout_anchor", bottom_left_block)
    SceneManager.insertWidget("debug_layout_anchor", bottom_right_block)
