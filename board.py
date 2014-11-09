from tiles import Tiles
from shape import Shape
from consts import shape_color
import random
from copy import deepcopy

class Board:
    def __init__(self, window, width=10, height=16, xinit=2, yinit=2, tile_width=15):
        self.tiles = Tiles(tile_width, window)
        self.window = window
        self.height = height
        self.xinit = xinit
        self.yinit = yinit
        self.width = width
        self.total_lines = 0
        self.board = [[0 for j in range(width)] for i in range(height)]
        self.shape = None
        self._draw()
        self.clear()

    def add_shape(self):
        assert not self.shape
        sh, col = random.choice(shape_color)
        self.shape = Shape(sh, self.window, col, self.width/2, 0, self.xinit, self.yinit)
        if self.collides(self.shape):
            raise GameOver()
        self.shape.draw()

    def eat_shape(self):
        self.shape.erase()
        for x,y in self.shape.shape:
            self.board[y+self.shape.y][x+self.shape.x] = 1
        self.shape = None

    def frame(self, pressed_keys):
        if not self.shape:
            return
        shapex = self.shape.x
        shapey = self.shape.y
        shape_shape = deepcopy(self.shape.shape)
        self.shape.update_pos(pressed_keys)
        if self.collides(self.shape):
            self.shape.x = shapex
            self.shape.y = shapey
            self.shape.shape = shape_shape
        else:
            self.shape.draw()

    def collides(self, shape):
        for x,y in shape.shape:
            x += shape.x
            y += shape.y
            if x < 0 or x >= self.width:
                return True
            if y >= self.height or y < 0:
                return True
            if self.board[y][x] == 1:
                return True
        return False

    def collides_bottom(self, shape):
        for x,y in shape.shape:
            x += shape.x
            y += shape.y
            if y+1 >= self.height:
                return True
            if self.board[y+1][x]:
                return True
        return False

    def tick(self):
        self._erase()
        if not self.shape:
            self.add_shape()
        elif not self.collides_bottom(self.shape):
            self.shape.erase()
            self.shape.move_down()
            self.shape.draw()

        elif self.collides_bottom(self.shape):
            self.eat_shape()
            self.check_lines()

        self._draw()

    def check_lines(self):
        for i in range(self.height):
            if self.check_line(self.board[i]):
                self.board.pop(i)
                self.total_lines += 1
                print self.total_lines
                self.board = [[0 for i in range(self.width)]] + self.board

    def check_line(self, line):
        for i in line:
            if not i:
                return False
        return True

    def _draw(self, draw_f=Tiles.square):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]:
                    draw_f(self.tiles, x+self.xinit, y+self.yinit)

    def _erase(self):
        self._draw(draw_f=Tiles.erase)

    def clear(self):
        for y in range(self.height):
            for x in range(self.width):
                self.tiles.erase(x+self.xinit, y+self.yinit)



class GameOver(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "You lose."
