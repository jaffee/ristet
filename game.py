import pygame
pygame.init()
import time
import engine_utils
from pygame.display import flip
from consts import dark_grey, FRAME
from board import Board

from tiles import Tiles
from shape import Shape

window = pygame.display.set_mode((640, 480))
pygame.draw.rect(window, dark_grey, ((0,0), (640,480)) )

def make_ticker(start_time, tick_amount):
    time = start_time
    while True:
        time += tick_amount
        yield time


def get_pressed_keys():
    pressed_keys = {}
    for ev in pygame.event.get():
        if ev.type == pygame.KEYDOWN:
            pressed_keys[ev.key] = 1
    return pressed_keys

game_tick = 1
if __name__ == "__main__":
    start = time.time()
    count = 0
    board = Board(window)
    board.clear()
    ticker = make_ticker(start, game_tick)
    next_tick = ticker.next()
    end_cond = False
    while not end_cond:
        count += 1
        if time.time() >= next_tick:
            next_tick = ticker.next()
            board.tick()
        pressed_keys = get_pressed_keys()
        board.frame(pressed_keys)
        engine_utils.do_sleep(start, count, FRAME)
        flip()
