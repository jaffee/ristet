import pygame
pygame.init()
import time
from engine_utils import make_ticker, get_pressed_keys, do_sleep
from pygame.display import flip
from consts import dark_grey, FRAME
from board import Board

from tiles import Tiles
from shape import Shape

window = pygame.display.set_mode((640, 480))
pygame.draw.rect(window, dark_grey, ((0,0), (640,480)) )

def main():
    game_tick = 1
    start = time.time()
    count = 0
    board = Board(window)
    ticker = make_ticker(start, game_tick)
    next_tick = ticker.next()
    while True:
        count += 1
        if time.time() >= next_tick:
            next_tick = ticker.next()
            board.tick()
        board.frame(get_pressed_keys())
        do_sleep(start, count, FRAME)
        flip()

if __name__ == "__main__":
    main()
