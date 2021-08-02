from typing import List, Dict, Optional, Any

Links = Dict["Cell", bool]
CellList = List["Cell"]

class Cell():
    """Represent a cell"""

    @property
    def row(self) -> int:
        return self._row

    @property
    def column(self) -> int:
        return self._column

    @property
    def links(self) -> CellList:
        return list(self._links.keys())

    @property
    def neighbors(self) -> CellList:
        """Returns list of all neighbors (north, east, south, west)"""

        neighbors: CellList = []
        if self.north():
            neighbors.append(self.north)
        if self.east():
            neighbors.append(self.east)
        if self.south():
            neighbors.append(self.south)
        if self.west():
            neighbors.append(self.west)
        return neighbors

    def __init__(self, row: int, column: int) -> None:
        self._row: int = row
        self._column: int = column
        self._links: Dict[Cell, bool] = {}
        self.north: Optional[Cell] = None
        self.east: Optional[Cell] = None
        self.south: Optional[Cell] = None
        self.west: Optional[Cell] = None

    def __repr__(self) -> str:
        return f'Cell(row={self._row}, column={self._column})'

    def link(self, cell, bidirectional=True) -> None:
        self._links[cell] = True
        if bidirectional:
            cell.link(self, bidirectional=False)

    def unlink(self, cell, bidirectional=True) -> None:
        del self._links[cell]
        if bidirectional:
            cell.unlink(self, bidirectional=False)

    def linked(self, cell) -> bool:
        """Returns if cell is in _links of cell"""

        return cell in self.links()

def is_cell(cell: Any) -> bool:
    return isinstance(cell, Cell)