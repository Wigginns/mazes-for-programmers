from cell import Cell

class Grid():
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = list()
        self.prepare_grid()
        self.configure_cells()

    def __getitem__(self, row, column):
        """Override [] accessor to return the Cell in _grid as long as it's within bounds"""
        print(row, column)
        if row in range(self._rows) and column in range(self._columns):
            return self._grid[row, column]


    def prepare_grid(self):
        for r in range(self._rows):
            for c in range(self._columns):
                self._grid.append(Cell(r,c))
        print(repr(self._grid))

    def configure_cells(self):
        for cell in self._grid:
            row, column = cell._row, cell._column

            # cell._north = self[row - 1, column]
            cell._north = self.__getitem__(row - 1, column)
            cell._south = self.__getitem__(row + 1, column)
            cell._east =  self.__getitem__(row, column + 1)
            cell._west =  self.__getitem__(row, column - 1)