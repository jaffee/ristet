import time
import pygame
import sys

def do_sleep(start, count, frame):
    sleep_until = frame*count + start
    try:
        time.sleep(sleep_until - time.time())
    except IOError:
        pass

def make_ticker(start_time, tick_amount):
    time = start_time
    while True:
        time += tick_amount
        yield time


def get_pressed_keys():
    # pygame.event.pump()
    # pressed =  pygame.key.get_pressed()
    # return {i: s for i,s in enumerate(pressed)}
    pressed_keys = {}
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT or (
                ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
            sys.exit()
        elif ev.type == pygame.KEYDOWN:
            pressed_keys[ev.key] = 1
    return pressed_keys
