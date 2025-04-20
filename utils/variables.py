
from button import font
from utils.var_col import *

FPS = 60

HEIGHT_ = 750
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

GAP_BUTTONS = 5
start_mes = "Start"
end_mes = "End" 
obstacle_mes = "Obstacle"
find_mes = "Find the shortest path"
delete_mes = "Delete"
clear_mes = "Clear All"
message_dimensions = [width_and_height(start_mes), width_and_height(end_mes), width_and_height(obstacle_mes), width_and_height(find_mes), width_and_height(delete_mes), width_and_height(clear_mes)]
# 5 gaps

START_W, START_H = message_dimensions[0]
START_X = WIDTH // 2 - (sum(x[0] for x in message_dimensions) + 5 * GAP_BUTTONS) // 2
START_Y = BAR_Y + BAR_HEIGHT // 2 - START_H // 2


END_W, END_H = message_dimensions[1]
END_X = START_X + START_W + GAP_BUTTONS
#END_Y = BAR_Y + BAR_HEIGHT // 2 - END_H // 2
END_Y = START_Y


OBSTACLE_W, OBSTACLE_H = message_dimensions[2]
OBSTACLE_X = END_X + END_W + GAP_BUTTONS
OBSTACLE_Y = START_Y


FIND_W, FIND_H = message_dimensions[3]
FIND_X = OBSTACLE_X + OBSTACLE_W + GAP_BUTTONS
FIND_Y = START_Y


DELETE_W, DELETE_H = message_dimensions[4]
DELETE_X = FIND_X  + FIND_W + GAP_BUTTONS
DELETE_Y = START_Y


CLEAR_W, CLEAR_H = message_dimensions[5]
CLEAR_X = DELETE_X + DELETE_W + GAP_BUTTONS
CLEAR_Y = START_Y