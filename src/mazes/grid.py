from typing import List
from cell import Cell

class Grid():
    _grid: List

    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = list()
        self.prepare_grid()
        self.configure_cells()

    # def __getitem__(self, row, column):
    #     """Override [] accessor to return the Cell in _grid as long as it's within bounds"""

    #     if row in range(self._rows) and column in range(self._columns):
    #         return self._grid[row][column]

    def _getCell(self, row, column):
        if row in range(self._rows) and column in range(self._columns):
            return self._grid[row][column]

    def prepare_grid(self):
        """Setup 2d array in _grid of Cells with Cell(r,c)"""

        self._grid = [[Cell(r,c) for c in range(self._columns)] for r in range(self._rows)]
        print(repr(self._grid))

    def configure_cells(self):
        for row in range(self._rows):
            for column in range(self._columns):
                # cell = list(self._grid)[row][column]
                cell = self._getCell(row, column)
                # cell = self[row, column]

                cell._north = self._getCell(row - 1, column)
                cell._south = self._getCell(row + 1, column)
                cell._east =  self._getCell(row, column + 1)
                cell._west =  self._getCell(row, column - 1)