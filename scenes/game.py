from novelib import SceneManager, ChatManager
from novelib.ui import widgets, Anchor, Sizing, Order, Link


def create() -> None:
    SceneManager.createScene("game_start")
    SceneManager.insertWidget(
        "game_start",
        widgets.Background(Anchor.TOPLEFT, Sizing.FILL, "assets/images/bg_menu.jpg"),
    )

    pause_modal: widgets.Modal = widgets.Modal(
        Anchor.CENTER, Sizing.COVER, "Pause Modal"
    )
    pause_modal.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Back to main menu.",
            Link.toScene("main_menu"),
        )
    )
    modal_idx: int = SceneManager.insertWidgetIdx("game_start", pause_modal)

    pause_block: widgets.Block = widgets.Block(
        Anchor.TOPLEFT,
        Sizing.COVER,
        Order.VERTICAL,
    )
    pause_block.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Pause.",
            Link.toModal(modal_idx),
        )
    )
    SceneManager.insertWidget("game_start", pause_block)

    trigger_block: widgets.Block = widgets.Block(
        Anchor.TOPRIGHT,
        Sizing.COVER,
        Order.VERTICAL,
    )
    trigger_block.addWidget(
        widgets.Button(
            Anchor.NONE,
            Sizing.COVER,
            "Trigger chat.",
            Link.toChat("start_1"),
        )
    )
    SceneManager.insertWidget("game_start", trigger_block)

    chat_block: widgets.Block = widgets.Block(
        Anchor.BOTTOM,
        Sizing.COVER,
        Order.VERTICAL,
    )
    chat_block.addWidget(
        widgets.ChatBox(
            Anchor.NONE,
            Sizing.COVER,
        )
    )
    SceneManager.insertChatBox("game_start", chat_block)
