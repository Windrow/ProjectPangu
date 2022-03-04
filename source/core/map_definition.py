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


class grid_square(grid):
    def __init__(self, x, y, id):
        grid.__init__(self, x, y, id)

        # neighbours
        self._nb_up = None
        self._nb_down = None
        self._nb_left = None
        self._nb_right = None


'''
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
'''



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

class pangu_map_column(pangu_map):
    # a circular column
    def __init__(self, width, height):
        pangu_map.__init__(self, width, height)

class pangu_map_sphere(pangu_map):
    # a circular column with one grid for each pole
    def __init__(self, width, height):
        pangu_map.__init__(self, width, height)



