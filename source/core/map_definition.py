# define grid object which is the smallest element of a map
# define grid group object which is a set of grids
# define map object which contains a two-dimension list of grid objects



# grid definition
class grid():
    def __init__(self, x, y, id):
        # position and identity
        self._pos_x = x
        self._pos_y = y
        self._id = id

        # grid_group
        self._group = None

    def setGroup(self, group_id):
        self._group = group_id


class grid_square(grid):
    def __init__(self, x, y, id):
        grid.__init__(self, x, y, id)

        # neighbours
        self._nb_up = None
        self._nb_down = None
        self._nb_left = None
        self._nb_right = None

    def setNeighbour(self, neighbour_up, neighbour_down, neighbour_left, neighbour_right):
        if neighbour_up is not None:
            self._nb_up = neighbour_up
        if neighbour_down is not None:
            self._nb_down = neighbour_down
        if neighbour_left is not None:
            self._nb_left = neighbour_left
        if neighbour_right is not None:
            self._nb_right = neighbour_right


class grid_hexagon(grid):
    def __init__(self, x, y, id):
        grid.__init__(self, x, y, id)

        # neighbours
        self._nb_0 = None
        self._nb_2 = None
        self._nb_4 = None
        self._nb_6 = None
        self._nb_8 = None
        self._nb_10 = None


class grid_pole(grid):
    def __init__(self, id):
        grid.__init__(self, -1, -1, id)

        # neighbours
        self._nb = []

    def addNeighbour(self, neighbour)
        self._nb.append(neighbour)


# grid group definition
class grid_group():
    def __init__(self, id):
        # identity
        self._id = id

        # members, edge, neighbours
        self._grid = []
        self._edge = []
        self._nb = []



# map definition
class pangu_map():
    def __init__(self, width, height):
        # width, height
        self._width = width
        self._height = height

        # 2d grid list
        self._map = []


class pangu_map_flat(pangu_map):
    # a rectangle
    def __init__(self, width, height):
        pangu_map.__init__(self, width, height)

        self._map = [[grid_square(i, j, i * width + j) for j in range(width)] for i in range(height)]
        self._map[0][0].setNeighbour(None, self._map[1][0], None, self._map[0][1])
        self._map[0][width - 1].setNeighbour(None, self._map[1][width - 1], self._map[0][width - 2], None)
        self._map[height - 1][0].setNeighbour(self._map[height - 2][0], None, None, self._map[height - 1][1])
        self._map[height - 1][width - 1].setNeighbour(self._map[height - 2][width - 1], None, self._map[height - 1][width - 2], None)
        for i in range(1, height - 1):
            self._map[i][0].setNeighbour(self._map[i - 1][0], self._map[i + 1][0], None, self._map[i][1])
            self._map[i][width - 1].setNeighbour(self._map[i - 1][width - 1], self._map[i + 1][width - 1], self._map[i][width - 2], None)
        for j in range(1, width - 1):
            self._map[0][j].setNeighbour(None, self._map[1][j], self._map[0][j - 1], self._map[0][j + 1])
            self._map[height - 1][j].setNeighbour(self._map[height - 2][j], None, self._map[height - 1][j - 1], self._map[height - 1][j + 1])
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                self._map[i][j].setNeighbour(self._map[i - 1][j], self._map[i + 1][j], self._map[i][j - 1], self._map[i][j + 1])


class pangu_map_column(pangu_map):
    # a circular column
    def __init__(self, width, height):
        pangu_map_flat.__init__(self, width, height)

        for i in range(height):
            self._map[i][0].setNeighbour(None, None, self._map[i][width - 1], None)
            self._map[i][width - 1].setNeighbour(None, None, None, self._map[i][0])


class pangu_map_sphere(pangu_map):
    # a circular column with one grid for each pole
    def __init__(self, width, height):
        pangu_map_column.__init__(self, width, height)

        self._np = grid_pole(0)
        self._sp = grid_pole(1)
        for j in range(width):
            self._map[0][j].setNeighbour(self._np, None, None, None)
            self._map[height - 1][j].setNeighbour(None, self._sp, None, None)
            self._np.addNeighbour(self._map[0][j])
            self._sp.addNeighbour(self._map[height - 1][j])


