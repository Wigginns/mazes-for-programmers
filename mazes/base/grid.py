import random
from typing import cast, List, Generator, Tuple, Optional
from .cell import Cell, is_cell

Key = Tuple[int, int]
CellList = List[Cell]
class Grid():

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def columns(self) -> int:
        return self._columns



    def __init__(self, rows, columns) -> None:
        if rows is None or rows < 2:
            raise ValueError("rows must be an int greater than 1")
        if columns is None or columns < 2:
            raise ValueError("columns must be an int greater than 1")

        self._rows: int = rows
        self._columns: int = columns
        self._grid: List[CellList] = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self) -> List[CellList]:
        """Setup 2d array in _grid of Cells with Cell(r,c)"""

        return [[Cell(r,c) for c in range(self._columns)] for r in range(self._rows)]

    def configure_cells(self):
        for row in range(self._rows):
            for column in range(self._columns):
                cell = self[row, column]

                cell.north = self[row - 1, column]
                cell.south = self[row + 1, column]
                cell.east = self[row, column - 1]
                cell.west = self[row, column + 1]

    def each_row(self) -> Generator[CellList, None, None]:
        for row in range(self.rows):
            yield self._grid[row]

    def each_cell(self) -> Generator:
        for row in self.each_row():
            for cell in row:
                yield cell

    def cell_at(self, row, column) -> Optional[Cell]:
        if row in range(self._rows) and column in range(self._columns):
            return self._grid[row][column]
        return None

    def set_cell_at(self, row: int, column: int, cell: Cell) -> None:
        self._grid[row][column] = cell

    def __getitem__(self, key: Key) -> Optional[Cell]:
        """Override [] accessor to return the Cell in _grid as long as it's within bounds"""

        if not is_key(key):
            raise IndexError('Only valid indexes ex. Grid[row,col] are supported')
        return self.cell_at(*key)

    def __setitem__(self, key: Key, new_cell: Cell) -> None:
        """Override [] setter to allow a key to set an item"""

        if not is_key(key):
            raise IndexError('Only valid indexes ex. Grid[row,col] are supported')
        if not is_cell(new_cell):
            raise ValueError('Only a Cell can be placed into the grid')
        self.set_cell_at(*key, new_cell)

    def random_cell(self) -> Cell:
        row = random.randrange(self.rows)
        column = random.randrange(self.columns)
        return cast(Cell, self[row, column])


def is_key(key: Key) -> bool:
    """
    Runtime check for key correctness
    """
    return type(key) == tuple and len(key) == 2 and not any(type(value) != int for value in key)