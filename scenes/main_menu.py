from novelib.ui import SceneManager, widgets, Anchor, Sizing, Link

SceneManager.createScene("main_menu")
SceneManager.insertWidget(
    "main_menu", widgets.Background(Anchor.DEFAULT, Sizing.FILL, "bg_menu")
)

menu_items: widgets.Block = widgets.Block(Anchor.CENTER, Sizing.COVER)

menu_items.addWidget(
    widgets.Button(
        Anchor.DEFAULT, Sizing.COVER, "Start Game", Link.toScene("game_start")
    )
)
menu_items.addWidget(
    widgets.Button(
        Anchor.DEFAULT, Sizing.COVER, "Settings", Link.toScene("main_menu_settings")
    )
)

SceneManager.insertWidget("main_menu", menu_items)

about_modal: widgets.Modal = widgets.Modal(Anchor.CENTER, Sizing.COVER, "About Page")
about_modal.addWidget(
    widgets.TextArea(Anchor.DEFAULT, Sizing.DEFAULT, "This is an about page.")
)

menu_about = widgets.Button(
    Anchor.BOT_LEFT, Sizing.COVER, "About", Link.toModal(about_modal)
)

SceneManager.insertWidget("main_menu", menu_about)
