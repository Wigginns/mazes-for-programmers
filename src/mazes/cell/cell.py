class Cell():
    """Represent a cell."""

    def __init__(self, row, column):
        self._row = row
        self._column = column
        self._links = {}

    def east():
        pass
    def west():
        pass
    def north():
        pass
    def south():
        pass

    @classmethod
    def link(self, cell, bidirectional=True):
        self._links[cell] = True
        if bidirectional:
            cell.link(self, bidirectional=False)

    @classmethod
    def unlink(self, cell, bidirectional=True):
        del self._links[cell]
        if bidirectional:
            cell.unlink(self, bidirectional=False)

    @classmethod
    def links(self):
        return self._links.keys()

    @classmethod
    def linked(self, cell):
        return cell in self.links()

    @classmethod
    def neighbors(self):
        neighbors = []
         #can I use _ instead of self.north() again?
        if self.north(): neighbors.append(self.north())
        if self.east(): neighbors.append(self.east())
        if self.south(): neighbors.append(self.south())
        if self.west(): neighbors.append(self.west())
