from pico2d import *
import game_framework

import play_mode
import select_mode
import tennis_mode

start_mode = select_mode

open_canvas(1200, 700)
game_framework.run(start_mode)
close_canvas()

