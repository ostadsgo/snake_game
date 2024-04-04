import sys
from random import randrange

import pygame
from pygame.math import Vector2

pygame.init()


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)]
        self.direction = Vector2(1, 0)
        self.head = self.body[0]

    def draw(self):
        for block in self.body:
            rect = pygame.Rect(
                block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            pygame.draw.rect(screen, (17, 76, 214), rect)

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, self.body[0] + self.direction)
        self.body = body_copy
        self.head = self.body[0]

    def grow(self):
        body_copy = self.body[:]
        body_copy.insert(0, self.body[0] + self.direction)
        self.body = body_copy
        self.head = self.body[0]

    def hit_wall(self):
        conditions = [
            not 0 <= self.head.x < CELL_NUBMER,
            not 0 <= self.head.y < CELL_NUBMER,
        ]
        return any(conditions)

    def hit_itself(self):
        return self.head in self.body[1:]


class Fruit:
    def __init__(self):
        self.new()
        self.img = pygame.image.load("./img/apple.png")

    def new(self):
        self.x = randrange(0, CELL_NUBMER)
        self.y = randrange(0, CELL_NUBMER)
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        # Rect(x, y, w, h)
        rect = pygame.Rect(
            self.pos.x * CELL_SIZE,
            self.pos.y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE,
        )
        screen.blit(self.img, rect)


class Main:
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake()

    def update(self):
        self.snake.move()
        self.eat()
        self.on_fail()

    def draw(self):
        self.snake.draw()
        self.fruit.draw()

    def eat(self):
        if self.fruit.pos == self.snake.head:
            self.fruit.new()
            self.snake.grow()

    def on_fail(self):
        if self.snake.hit_wall():
            self.game_over()
        if self.snake.hit_itself():
            self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()


# Constants
CELL_SIZE = 40
CELL_NUBMER = 15
WIDTH = CELL_SIZE * CELL_NUBMER
HEIGHT = CELL_SIZE * CELL_NUBMER
FPS = 60
SCREEN_UPDATE = pygame.USEREVENT

# variables
running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.time.set_timer(SCREEN_UPDATE, 150)
main = Main()

# game loop
while running:
    # Event / User input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.snake.direction.y != 1:
                    main.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main.snake.direction.y != -1:
                    main.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main.snake.direction.x != 1:
                    main.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main.snake.direction.x != -1:
                    main.snake.direction = Vector2(1, 0)

    # Elements
    screen.fill((175, 215, 70))
    main.draw()
    pygame.display.update()
    clock.tick(FPS)

main.game_over()
