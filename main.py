import pygame as pg
from novelib import SceneManager
from scenes import main_menu


def loop(window: pg.Surface, clock: pg.time.Clock) -> None:
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            SceneManager.handleEvent(event)

        window.fill((0, 0, 0))
        SceneManager.drawScene(window)
        pg.display.flip()

        clock.tick(60)


def main() -> None:
    main_menu.create()
    
    pg.init()
    window: pg.Surface = pg.display.set_mode((800, 600), pg.RESIZABLE)
    pg.display.set_caption("Window")

    clock: pg.time.Clock = pg.time.Clock()

    SceneManager.loadScene("main_menu")

    loop(window, clock)

    pg.quit()


if __name__ == "__main__":
    main()
