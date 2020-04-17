from random_move import generate_random_move
from maze import Maze

def maze_mover(maze):
    running = True
    solution_path = []
    current_position = maze.tiles[maze.start]
    while running:
        if current_position == maze.tiles[maze.end]:
            running = False
        
        solution_path.append(current_position)
        next_direction = generate_random_move(current_position)
        if next_direction == "left":
            next_position = current_position.left
        if next_direction == "right":
            next_position = current_position.right
        if next_direction == "up":
            next_position = current_position.up
        if next_direction == "down":
            next_position = current_position.down
        current_position = next_position
    
    #print(solution_path)
    #print(len(solution_path))
    #print(solution_path[-1].position)
    return len(solution_path)


# Everything Below is just for testing
test_maze = Maze(5, 0, 21)
test_maze.fill_maze()


test_maze.tiles[5].passable = False
test_maze.tiles[6].passable = False
test_maze.tiles[8].passable = False
test_maze.tiles[13].passable = False
test_maze.tiles[16].passable = False
test_maze.tiles[17].passable = False
test_maze.tiles[18].passable = False
test_maze.tiles[22].passable = False

total_moves = 0
for x in range(10000): 
    total_moves += maze_mover(test_maze)
total_moves /= 10000

# Prints out a picture of maze
simple_maze = []
row = []
column = 0
for key, tile in test_maze.tiles.items():
    if tile.passable == True:
        spot = "o"
    else:
        spot = "x"
    row.append(spot)
    if column == test_maze.size - 1:
        simple_maze.append(row)
        column = 0
        print(row)
        row = []
    else:
        column += 1
print(total_moves)

