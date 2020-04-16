from random import choice
from tile import Tile


def generate_random_move(current_tile):
    possible_move_directions = []
    if current_tile.up != None and current_tile.up.passable == True:
        possible_move_directions.append("up")
    if current_tile.right != None and current_tile.right.passable == True:
        possible_move_directions.append("right")
    if current_tile.down != None and current_tile.down.passable == True:
        possible_move_directions.append("down")
    if current_tile.left != None and current_tile.left.passable == True:
        possible_move_directions.append("left")
    return choice(possible_move_directions)
