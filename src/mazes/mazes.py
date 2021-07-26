from cell import Cell

c = Cell(1,2)

print(vars(c))

c2 = Cell(1,3)

c.link(c2)

print(c.links())
