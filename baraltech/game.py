import pygame as pg
from pygame.math import Vector2 as Vect


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.body = [Vect(5, 5), Vect(4, 5), Vect(3, 5)]
        self.direction = Vect(1, 0)
        self.head = self.body[0]

    def draw(self):
        cell_size = 25
        for block in self.body:
            rect = pg.Rect(
                block.x * cell_size + 1, block.y * cell_size, cell_size - 1 , cell_size
            )
            pg.draw.rect(self.screen, "green", rect)

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, self.body[0] + self.direction)
        self.body = body_copy
        self.head = self.body[0]


class Food:
    pass


class Game:
    def __init__(self):
        pg.init()
        self.width = 500
        self.height = 500
        screen_size = (self.width, self.height)
        self.screen = pg.display.set_mode(screen_size)
        self.clock = pg.time.Clock()
        self.fps = 10

    def draw_grid(self):
        cell_size = 25
        row_size = self.width // cell_size
        col_size = self.height // cell_size
        for y in range(row_size):
            pg.draw.line(
                self.screen, "#d6d6d6", (0, y * cell_size), (self.width, y * cell_size)
            )

        for x in range(col_size):
            pg.draw.line(
                self.screen, "#cccccc", (x * cell_size, 0), (x * cell_size, self.height)
            )

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def run(self):
        snake = Snake(self.screen)
        running = True
        while running:
            # check event
            self.check_event()
            # draw
            self.draw_grid()
            snake.draw()
            # update
            pg.display.flip()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()
