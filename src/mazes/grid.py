from cell import Cell

class Grid():
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        for r in self._rows:
            for c in self._columns:
                self._grid.append(Cell(r,c))

    def configure_cells(self):
        for cell in self._grid:
            cell._north = [self._row - 1, self._column],
            cell._south = [self._row + 1, self._column],
            cell._east =  [self._row, self._column + 1],
            cell._west =  [self._row, self._column - 1],