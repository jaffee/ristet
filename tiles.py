import pygame
from consts import black, white




class Tiles:
    def __init__(self, square_size, window, color=white):
        self.square_size = square_size
        self.window = window
        self.color = color
        self.bgcolor = black

    def _draw(self, *args, **kwargs):
        pygame.draw.rect(self.window, *args, **kwargs)

    def _get_color(self, color):
        if not color:
            return self.color
        else:
            return color

    def square(self, x, y, color=None):
        upper_left = (x*self.square_size, y*self.square_size)
        lower_right = (self.square_size, self.square_size)
        self._draw(self._get_color(color), (upper_left, lower_right))

    def erase(self, x, y):
        upper_left = (x*self.square_size, y*self.square_size)
        lower_right = (self.square_size, self.square_size)
        self._draw(self.bgcolor, (upper_left, lower_right))
