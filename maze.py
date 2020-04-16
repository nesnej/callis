from tile import Tile


class Maze:

    def __init__(self, size):
        self.size = size
        self.tiles = {}

    def fill_maze(self):
        tile_counter = 0
        row = 0
        column = 0
        for num in range(self.size**2):
            l_tile = tile_counter - 1
            r_tile = tile_counter + 1
            u_tile = tile_counter - self.size
            d_tile = tile_counter + self.size

            tile = Tile()

            if column > 0:
                tile.left = self.tiles[l_tile]
                self.tiles[l_tile].right = tile
            if row > 0:
                tile.up = self.tiles[u_tile]
                self.tiles[u_tile].down = tile

            self.tiles[tile_counter] = tile
            tile.position = tile_counter
            tile_counter += 1

            if column == self.size - 1:
                column = 0
                row += 1
            else:
                column += 1


maze = Maze(5)
maze.fill_maze()
maze.tiles[2].passable = False
maze.tiles[5].passable = False
maze.tiles[7].passable = False
maze.tiles[9].passable = False
maze.tiles[10].passable = False
maze.tiles[17].passable = False
maze.tiles[18].passable = False
maze.tiles[22].passable = False


simple_maze = []
row = []
column = 0
for key, tile in maze.tiles.items():
    if tile.passable == True:
        spot = "o"
    else:
        spot = "x"
    row.append(spot)
    if column == maze.size - 1:
        simple_maze.append(row)
        column = 0
        print(row)
        row = []
    else:
        column += 1
