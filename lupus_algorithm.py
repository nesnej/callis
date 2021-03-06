from maze import Maze


def lupus_algorithm(maze):
    solution_path = []
    current_position = maze.tiles[maze.start]
    start_column_spot = current_position
    right_openings = []
    left_openings = []
    up_down_openings = []
    current_up = True
    while True:
        solution_path.append(current_position)

        if current_position == maze.tiles[maze.end]:
            break

        # Checks to see if the position to right is open and not added already then will add to right_openings if both are true
        if current_position.right != None and current_position.right.passable == True:
            already_added = False
            if right_openings:
                for right in right_openings:
                    if current_position.right == right:
                        already_added = True
            if already_added == False:
                right_openings.append(current_position.right)

        # Checks to see if the position to left is open and not added already then will add to left_openings if both are true
        if current_position.left != None and current_position.left.passable == True:
            already_added = False
            if left_openings:
                for left in left_openings:
                    if current_position.left == left:
                        already_added = True
            if already_added == False:
                left_openings.append(current_position.left)

        if current_up == True:
            already_added = False
            if up_down_openings:
                for position in up_down_openings:
                    if current_position.up == position:
                        already_added = True
            if already_added == False and current_position.up != None and current_position.up.passable == True:
                next_position = current_position.up
                current_position = next_position
                up_down_openings.append(current_position)
            else:
                current_up = False
                current_position = start_column_spot
        else:
            already_added = False
            if up_down_openings:
                for position in up_down_openings:
                    if current_position.down == position:
                        already_added = True
            if already_added == False and current_position.down != None and current_position.down.passable == True:
                next_position = current_position.down
                current_position = next_position
                up_down_openings.append(current_position)
            # Takes your current position to one of the right or left openings
            else:
                current_up = True
                if right_openings:
                    current_position = right_openings[0]
                    del right_openings[0]
                elif left_openings:
                    current_position = left_openings[0]
                    del left_openings[0]

                start_column_spot = current_position
    solution_path = list(dict.fromkeys(solution_path))
    return solution_path


# Testing below
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


print(lupus_algorithm(test_maze))
