import time
import pygame

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
    pressed_keys = {}
    for ev in pygame.event.get():
        if ev.type == pygame.KEYDOWN:
            pressed_keys[ev.key] = 1
    return pressed_keys
