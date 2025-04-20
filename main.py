import pygame
from utils import *
from algorithm import *
from button import *
from sys import exit

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT_))
pygame.display.set_caption("A* path finder")

gameIcon = pygame.image.load("icon.ico")
pygame.display.set_icon(gameIcon)

obstacles = []
costs = []
start_node = None
end_node = None
visited_nodes = set()
s = None
e = None

path = []
frontier = []


def draw_grid(win, n):
    for i in range(n + 1):
        pygame.draw.line(win, BLACK, (0, i * GAP_Y), (WIDTH, i * GAP_Y), 1)
        pygame.draw.line(win, BLACK, (i * GAP_X, 0), (i * GAP_X, HEIGHT), 1)


start_but = Button(START_X, START_Y, start_mes, "start")
end_but = Button(END_X, END_Y, end_mes, "end")
obstacle_but = Button(OBSTACLE_X, OBSTACLE_Y, obstacle_mes, "obstacle")
find_but = Button(FIND_X, FIND_Y, find_mes, "find")
delete_but = Button(DELETE_X, DELETE_Y, delete_mes, "delete")
clear_but = Button(CLEAR_X, CLEAR_Y, clear_mes, "clear")


def check_current_task(mouse_x, mouse_y, event):
    global current_task
    if start_but.is_clicked(mouse_x, mouse_y, event):
        current_task = start_but.role
    if end_but.is_clicked(mouse_x, mouse_y, event):
        current_task = end_but.role
    if obstacle_but.is_clicked(mouse_x, mouse_y, event):
        current_task = obstacle_but.role
    if find_but.is_clicked(mouse_x, mouse_y, event):
        current_task = find_but.role
    if delete_but.is_clicked(mouse_x, mouse_y, event):
        current_task = delete_but.role
    if clear_but.is_clicked(mouse_x, mouse_y, event):
        current_task = clear_but.role


def set_nodes(current_task, mouse_x, mouse_y):
    global costs, start_node, end_node, s, e, obstacles, path, frontier
    def is_mouse_event(mouse_pressed):
        if mouse_pressed[0]:
                return True
        return False

    def is_in_frame():
        return 0 <= mouse_x <= WIDTH and 0 <= mouse_y < HEIGHT

    if is_mouse_event(mouse_pressed):
        if is_in_frame():
            col = mouse_x // GAP_X 
            row = mouse_y // GAP_Y
            if current_task == start_but.role:
                s = row, col             
                start_node_x = col * GAP_X
                start_node_y = row * GAP_Y
                start_node = start_node_x, start_node_y
                costs = initialize_costs(NODES_N, s)

            elif current_task == end_but.role:
                e = row, col
                end_node_x = col * GAP_X
                end_node_y = row * GAP_Y
                end_node =  end_node_x, end_node_y  


            elif current_task == obstacle_but.role:
                node = row, col
                if node not in obstacles:
                    obstacles.append(node)

            elif current_task == delete_but.role:
                if (row, col) == s:
                    s = None
                    start_node = None
                elif (row, col) == e:
                    e = None
                    end_node = None
                elif (row, col) in obstacles:
                    obstacles.remove((row, col))

        if current_task == clear_but.role:
            s = None
            start_node = None
            e = None
            end_node = None
            obstacles = []
            path = []
            frontier = []


def draw_frontier(win):
    for n in frontier:
        pygame.draw.rect(win, YELLOW, (n[1][1] * GAP_X, n[1][0] * GAP_Y, GAP_X, GAP_Y))


def draw_path(win):
    for n in path:
        pygame.draw.rect(win, DARK_BLUE, (n[1] * GAP_X, n[0] * GAP_Y, GAP_X, GAP_Y)) 


def draw_visited_nodes(win):
    if len(visited_nodes) > 0:
        win.fill(GRAY_BAR)
        for node in visited_nodes:
            if node != s:
                pygame.draw.rect(win, WHITE, (node[1] * GAP_X, node[0] * GAP_X, GAP_X, GAP_Y))


def draw_nodes(win):
    if start_node: # if exists
        pygame.draw.rect(win, GREEN, (start_node[0], start_node[1], GAP_X, GAP_Y))
    if end_node:
        pygame.draw.rect(win, RED, (end_node[0], end_node[1], GAP_X, GAP_Y))
    for obs in obstacles:
        pygame.draw.rect(win, BLACK, (obs[1] * GAP_X, obs[0] * GAP_Y, GAP_X, GAP_Y))


msg = font.render("ESC to stop searching", True, BLACK)
def control_bar(win, mouse_x, mouse_y, mouse_pressed):
    pygame.draw.rect(win, GRAY_BAR, (0, BAR_Y, WIDTH, BAR_HEIGHT))
    pygame.draw.rect(win, BLACK, (0, BAR_Y, WIDTH, BAR_HEIGHT), BAR_THIC)
    start_but.draw(win, mouse_x, mouse_y, mouse_pressed)
    end_but.draw(win, mouse_x, mouse_y, mouse_pressed)
    obstacle_but.draw(win, mouse_x, mouse_y, mouse_pressed)
    find_but.draw(win, mouse_x, mouse_y, mouse_pressed)
    delete_but.draw(win, mouse_x, mouse_y, mouse_pressed)
    clear_but.draw(win, mouse_x, mouse_y, mouse_pressed)
    win.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT_ - msg.get_height() - BAR_THIC - 1))


def screen_draw(win, mouse_x, mouse_y, mouse_pressed):
    win.fill(WHITE)
    draw_visited_nodes(win)
    draw_frontier(win)
    draw_nodes(win)
    draw_path(win)
    draw_grid(win, NODES_N)
    control_bar(win, mouse_x, mouse_y, mouse_pressed)
    pygame.display.update()


def get_path(node):
    index = 0
    path = [node]
    distance = get_distance_from_start(node, costs)
    while distance > 0:
        succ = find_neighbors(path[-1], [], (NODES_N, NODES_N), obstacles)
        for s in succ:
            new_distance = get_distance_from_start(s,costs)
            if new_distance < distance:
                path.append(s)
                distance = new_distance
                index += 1 
                break
        pygame.draw.rect(window, DARK_BLUE, (path[index][1] * GAP_X, path[index][0] * GAP_Y, GAP_X, GAP_Y))
        pygame.draw.rect(window, BLACK, (path[index][1] * GAP_X, path[index][0] * GAP_Y, GAP_X, GAP_Y), 1)
        pygame.display.update() # path animation
    return path[1:len(path) - 1]


def astart(screen_draw, start, end, obstacles, size, event):
    global costs, frontier, visited_nodes, path
    frontier = []
    visited_nodes = set()
    heapq.heappush(frontier, (0, start))
    while len(frontier) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    path = []
                    visited_nodes = set()
                    frontier = []
                    return False
        priority, node = heapq.heappop(frontier)
        if node == end:
            path = get_path(end)
            return True
        visited_nodes.add(node)
        succ = find_neighbors(node, visited_nodes, size, obstacles)
        distance = get_distance_from_start(node, costs)
        new_distance = distance + 1
        for s in succ:
            if new_distance < get_distance_from_start(s, costs):
                costs[s[0]][s[1]] = new_distance
                frontier = [n for n in frontier if n != s]
                distance_to_end = distance_heuristic(node, end)
                heapq.heappush(frontier, (new_distance + distance_to_end, s))
        screen_draw()
    return False


current_task = None

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_x , mouse_y = pygame.mouse.get_pos()

    if current_task != find_but.role:
        path = []
        visited_nodes = set()
        frontier = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if find_but.is_clicked(mouse_x, mouse_y, event):
            if s and e and (s not in obstacles and e not in obstacles): # if start point and end point exist
                path = []
                astart(lambda: screen_draw(window, mouse_x, mouse_y, mouse_pressed), s, e, obstacles, (NODES_N, NODES_N), event)
                costs = initialize_costs(NODES_N, s) # reset costs

        check_current_task(mouse_x, mouse_y, event)

    set_nodes(current_task, mouse_x, mouse_y)
    screen_draw(window, mouse_x, mouse_y, mouse_pressed)
pygame.quit()
