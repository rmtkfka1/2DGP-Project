from pico2d import *


from tennis import select_mode, tennis_title
from share import game_framework

open_canvas(1200, 700)
game_framework.run(select_mode)
close_canvas()

