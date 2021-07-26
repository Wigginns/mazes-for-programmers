class Cell():
    """Represent a cell"""

    def __init__(self, row, column):
        self._row = row
        self._column = column
        self._links = {}
        self._north = None
        self._east = None
        self._south = None
        self._west = None
        # self._neighbors = {"north": None, "east": None, "south": None, "west": None,}

    def link(self, cell, bidirectional=True):
        self._links[cell] = True
        if bidirectional:
            cell.link(self, bidirectional=False)

    def unlink(self, cell, bidirectional=True):
        del self._links[cell]
        if bidirectional:
            cell.unlink(self, bidirectional=False)


    def links(self):
        """Returns KeysView of cells that are linked to cell"""

        return self._links.keys()

    def linked(self, cell) -> bool:
        """Returns if cell is in _links of cell"""

        return cell in self.links()

    def neighbors(self) -> list:
        """Returns list of all neighbors (north, east, south, west)"""

        neighbors = []
         #can I use _ instead of self.north() again?
        if self.north(): neighbors.append(self.north())
        if self.east(): neighbors.append(self.east())
        if self.south(): neighbors.append(self.south())
        if self.west(): neighbors.append(self.west())
        return neighbors
