import pygame
from consts import TILE_SIZE
from tiles import Tiles

class Shape:
    def __init__(self, shape, window, color, xinit, yinit, xdraw_offset, ydraw_offset):
        """shape is a list of tuples describing the shape [(0,0), (0,1), (0,2), (0,3)] would be a vertical bar"""
        self.shape = shape
        self.tiles = Tiles(TILE_SIZE, window, color)
        self.x = xinit
        self.y = yinit
        self.xdraw_offset = xdraw_offset
        self.ydraw_offset = ydraw_offset
        self.keymap = {pygame.K_a: self.move_left,
                       pygame.K_s: self.move_down,
                       pygame.K_d: self.move_right,
                       pygame.K_w: self.rot_right}

    def draw(self):
        for coord in self.shape:
            self.tiles.square(self.dx() + coord[0], self.dy()+coord[1])

    def erase(self):
        for coord in self.shape:
            self.tiles.erase(self.dx() + coord[0], self.dy()+coord[1])


    def dx(self):
        return self.x + self.xdraw_offset

    def dy(self):
        return self.y + self.ydraw_offset

    def rot_right(self):
        sh = self.shape
        ymax = max([p[1] for p in sh])
        ret = []
        for p in sh:
            ret.append((ymax-p[1], p[0]))
        self.shape = ret


    def move_right(self, amount=1):
        self.x += amount

    def move_left(self, amount=1):
        self.x -= amount

    def move_up(self, amount=1):
        self.y -= amount

    def move_down(self, amount=1):
        self.y += amount

    def update(self, pressed_keys):
        self.erase()
        self.update_pos(pressed_keys)
        self.draw()

    def update_pos(self, pressed_keys):
        for k in self.keymap:
            if pressed_keys.get(k):
                self.erase()
                self.keymap[k]()
