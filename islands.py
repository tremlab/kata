def count_islands(grid):
    """Accepts a 2D array (a list of lists) whose elements each 
        have the value of 1 or 0.
        Counts how many 'island' clusters of contiguous 1's.
    """
    cell_grid = Grid()

    n_columns = len(grid[0])
    n_rows = len(grid)

    # build Grid object from grid input
    for x in range(n_columns): 
        for y in range(n_rows):
            # keep row v col straight!
            value = grid[y][x]
            # only adding the 1s, no need to create cell for 0.
            if value == 1:
                # x is the horizontal, y the vertical
                new_cell = Cell(value, (x, y))
                cell_grid.add_cell(new_cell)

    # count islands in Grid object.
    count = cell_grid.count_islands()

    return count


class Cell(object):

    def __init__(self, value, location):
        #location is a tuple (x, y)
        self.value = value
        self.location = location


class Grid(object):
    
    def __init__(self):
        # dictionary for faster search.  (x,y) location is key.
        self.cells = {}
        self.available_cells = set([]) 

    def add_cell(self, cell):
        self.cells[cell.location] = cell

    def get_adjacents(self, cell):
        x, y = cell.location
        adjacents = []
        locations_to_check = [
            (x, y + 1),
            (x, y - 1),
            (x + 1, y),
            (x - 1, y),
        ]

        for l in locations_to_check:
            # dynamically checks if there are any adjacent cells
            # that haven't already been seen.
            if l in self.available_cells:
                adjacents.append(self.cells[l].location)
        # returns a LIST of the tuple locations of adjacent cells.
        return adjacents

    def count_islands(self):
        count = 0
        self.available_cells = set(self.cells.keys())

        while (self.available_cells):
            starting_point = self.available_cells.pop()
            self.remove_island(starting_point)
            count += 1
        return count

    def remove_island(self, starting_point):
        # find the cell with this location key.
        starting_cell = self.cells[starting_point]
        adjacents = self.get_adjacents(starting_cell)

        for a in adjacents:
            self.available_cells.discard(a)
            self.remove_island(a)

        # nothing to return or count, just removing all parts of the island

        return None
