white  = (255, 255, 255)
black  = (0, 0, 0)
red    = (255, 0, 0)
green  = (0, 255, 0)
blue   = (0, 0, 255)
bg     = (0, 255, 255)
rg     = (255, 255, 0)
pink = (255, 0, 255)
grey = (180, 180, 180)
dark_grey = (80, 80, 80)

# Shapes
sh_square = [(0,0), (0,1), (1,0), (1,1)]
sh_line   = [(0,0), (0,1), (0,2), (0,3)]
sh_z      = [(0,0), (1,0), (1,1), (2,1)]
sh_s      = [(1,0), (2,0), (0,1), (1,1)]
sh_t      = [(1,0), (0,1), (1,1), (2,1)]
sh_l      = [(0,0), (0,1), (0,2), (1,2)]
sh_revl   = [(1,0), (1,1), (1,2), (0,2)]

shape_list = [ sh_square, sh_line, sh_z, sh_s, sh_t, sh_l, sh_revl]
color_list = [ red,       green,   blue, bg,   rg,   pink, grey]
assert len(shape_list) == len(color_list)
shape_color = zip(shape_list, color_list)

FRAME = 1.0/60.0 # frame rate

TILE_SIZE = 15
