import pygame as pg


class Snake:
    def __init__(self):
        pass


class Color:
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


class Main:
    def __init__(self):
        pg.init()
        self.width = 500
        self.height = 500
        SCREEN_SIZE = (self.width, self.height)
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.FPS = 60

    def run(self):
        snake = Snake(Color.GREEN, (10, 10))
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            pg.time.delay(50)
            self.screen.fill(Color.BLACK)
            # draw grid
            self.draw_grid_line()

            pg.display.update()
            self.clock.tick(self.FPS)
        pg.quit()

    def draw_grid_line(self):
        cell_size = 20
        row_size = self.width // cell_size
        col_size = self.height // cell_size
        # draw rows
        for y in range(row_size):
            pg.draw.line(
                self.screen,
                Color.WHITE,
                (0, y * cell_size),
                (self.width, y * cell_size),
            )

        # draw columns
        for x in range(col_size):
            pg.draw.line(
                self.screen,
                Color.WHITE,
                (x * cell_size, 0),
                (x * cell_size, self.height),
            )


def main():
    main = Main()
    main.run()


if __name__ == "__main__":
    main()
