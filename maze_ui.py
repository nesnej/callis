import pygame
from maze import Maze
from tile import Tile
from lupus_algorithm import lupus_algorithm

# Pygame initialization
board_width = 800
board_height = 800
pygame.init()
screen = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("Maze Solver")
icon = pygame.image.load('mze.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


# Creaate a maze for testing purposes
maze = Maze(20, 0, 349)
maze.fill_maze()
maze.tiles[2].passable = False
maze.tiles[5].passable = False
maze.tiles[7].passable = False
maze.tiles[9].passable = False
maze.tiles[10].passable = False
maze.tiles[17].passable = False
maze.tiles[18].passable = False
maze.tiles[22].passable = False
maze.tiles[240].passable = False
maze.tiles[241].passable = False
maze.tiles[242].passable = False
maze.tiles[243].passable = False
maze.tiles[244].passable = False
maze.tiles[245].passable = False
maze.tiles[246].passable = False
maze.tiles[247].passable = False
maze.tiles[248].passable = False
maze.tiles[250].passable = False
maze.tiles[251].passable = False
maze.tiles[252].passable = False
maze.tiles[253].passable = False
maze.tiles[254].passable = False
maze.tiles[255].passable = False
maze.tiles[256].passable = False
maze.tiles[257].passable = False
maze.tiles[258].passable = False
maze.tiles[259].passable = False
maze.tiles[31].passable = False
maze.tiles[32].passable = False
maze.tiles[33].passable = False
maze.tiles[34].passable = False
maze.tiles[35].passable = False
maze.tiles[36].passable = False
maze.tiles[37].passable = False
maze.tiles[38].passable = False
maze.tiles[39].passable = False
maze.tiles[40].passable = False
maze.tiles[61].passable = False
maze.tiles[62].passable = False
maze.tiles[63].passable = False
maze.tiles[64].passable = False
maze.tiles[65].passable = False
maze.tiles[66].passable = False
maze.tiles[67].passable = False
maze.tiles[68].passable = False


# Test solution path list
t2 = maze.tiles[1]
t3 = maze.tiles[6]
t4 = maze.tiles[11]
t5 = maze.tiles[12]
t6 = maze.tiles[13]
t7 = maze.tiles[14]
t8 = maze.tiles[19]
t9 = maze.tiles[24]
solution_path = [t2, t3, t4, t5, t6, t7, t8, t9]

# Colors
blocked_color = (222, 111, 131)
open_color = (141, 14, 142)
goal_color = (51, 55, 211)
path_color = (155, 133, 89)

# Rectangle attributes
rectangle_height = round(board_width / maze.size, 0)
rectangle_width = round(board_width / maze.size, 0)

current_top = 0
current_left = 0

for i, tile in maze.tiles.items():
    r = pygame.Rect(current_left, current_top,
                    rectangle_width, rectangle_height)
    tile.rec = r
    current_left += rectangle_width
    if current_left > board_width - rectangle_width:
        current_left = 0
        current_top += rectangle_height

for i, tile in maze.tiles.items():
    if tile.position == maze.start or tile.position == maze.end:
        pygame.draw.rect(screen, goal_color, tile.rec)
    elif tile.passable == True:
        pygame.draw.rect(screen, open_color, tile.rec)
    else:
        pygame.draw.rect(screen, blocked_color, tile.rec)
    current_left += rectangle_width
    if current_left > board_width - rectangle_width:
        current_left = 0
        current_top += rectangle_height

solution_path = lupus_algorithm(maze)
del solution_path[0]
del solution_path[-1]
for tile in solution_path:
    pygame.draw.rect(screen, path_color, tile.rec)

running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()


pygame.quit()
