from mazesforprogrammers import Cell
from mazesforprogrammers.base.cell import is_cell


def test_cell():
    c = Cell(1, 2)
    c2 = Cell(1, 3)
    c3 = Cell(3, 4)

    assert c._row == 1
    assert c._column == 2
    assert len(c.links) == 0

    c2.link(c3)
    c.link(c2)
    c.linked(c2) == (True)
    assert c2.linked(c3)

    c.unlink(c2)
    assert not c.linked(c2)
    assert not c.linked(c3)

    c.north = c2
    assert c2 in c.neighbors
    assert c3 not in c.neighbors

    assert repr(c.north) == "Cell(1,3)"

    assert is_cell(c)
    assert not is_cell("I'm a sentence.")
