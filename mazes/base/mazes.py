from cell import Cell, is_cell
from grid import Grid

g = Grid(4,4)

c = g[2,2]
g[2,2] = Cell(2,2)

cc = g.random_cell()

print(is_cell(cc))
print(vars(cc))

# print(repr(c.north))

# c = g._getCell(4,4)

# print(repr(c._north))

