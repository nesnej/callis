class Tile:

    def __init__(self, left=None, right=None, up=None, down=None, passable=True):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.passable = passable
        self.position = None