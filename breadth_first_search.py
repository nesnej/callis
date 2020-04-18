from maze import Maze

class Node:

    def __init__(self, position=None, tile_type=None, up=None, down=None, right=None, left=None):
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.position = position
        self.tile_type = tile_type

def node_network(maze):
    for tile in maze.tiles:
        

