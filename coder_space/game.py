import pygame as pg
from random import randrange



WIDTH = 500
HEIGHT = 500
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

running = True
while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    screen.fill('black')
    pg.display.flip()
    clock.tick(60)

pg.quit()
exit()

