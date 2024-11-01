from novelib import SceneManager
from novelib.ui import widgets, Anchor, Sizing, Order, Link

SceneManager.createFont("Minecraftia", "Minecraftia-Regular.ttf", 24)
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
        Anchor.TOP,
        Sizing.COVER,
        "Start Game",
        Link.toScene("game_start"),
    )
)
menu_items.addWidget(
    widgets.Button(
        Anchor.BOTTOM,
        Sizing.COVER,
        "Settings",
        Link.toScene("main_menu_settings"),
        font=SceneManager.getFont("PressStart"),
    )
)

SceneManager.insertWidget("main_menu", menu_items)

# about_modal: widgets.Modal = widgets.Modal(Anchor.CENTER, Sizing.COVER, "About Page")
# about_modal.addWidget(
#     widgets.TextArea(Anchor.CENTER, Sizing.FILL, "This is an about page.")
# )

# menu_about = widgets.Button(
#     Anchor.BOTTOMLEFT,
#     Sizing.COVER,
#     "About",
#     Link.toModal(about_modal),
# )

# SceneManager.insertWidget("main_menu", menu_about)
