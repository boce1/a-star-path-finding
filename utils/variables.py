
from utils.button import font
from utils.var_col import *

FPS = 60

HEIGHT_ = 900
BAR_HEIGHT = 100
HEIGHT = HEIGHT_ - BAR_HEIGHT
WIDTH = HEIGHT

BAR_Y = HEIGHT_ - BAR_HEIGHT
BAR_THIC = 3

NODES_N = 50
GAP_X = WIDTH // NODES_N
GAP_Y = HEIGHT // NODES_N

def width_and_height(string):
    s = font.render(string, True, BLACK)
    return s.get_width() + BUTTON_GAP, s.get_height() + BUTTON_GAP

GAP_BUTTONS = 10

start_mes = "Start"
START_W, START_H = width_and_height(start_mes)
START_X = 25
START_Y = BAR_Y + BAR_HEIGHT // 2 - START_H // 2

end_mes = "End" 
END_W, END_H = width_and_height(end_mes)
END_X = START_X + START_W + GAP_BUTTONS
#END_Y = BAR_Y + BAR_HEIGHT // 2 - END_H // 2
END_Y = START_Y

obstacle_mes = "Obstacle"
OBSTACLE_W, OBSTACLE_H = width_and_height(obstacle_mes)
OBSTACLE_X = END_X + END_W + GAP_BUTTONS
OBSTACLE_Y = START_Y

find_mes = "Find the shortest path"
FIND_W, FIND_H = width_and_height(find_mes)
FIND_X = OBSTACLE_X + OBSTACLE_W + GAP_BUTTONS
FIND_Y = START_Y

delete_mes = "Delete"
DELETE_W, DELETE_H = width_and_height(delete_mes)
DELETE_X = FIND_X  + FIND_W + GAP_BUTTONS
DELETE_Y = START_Y

clear_mes = "Clear All"
CLEAR_W, CLEAR_H = width_and_height(clear_mes)
CLEAR_X = DELETE_X + DELETE_W + GAP_BUTTONS
CLEAR_Y = START_Y