import pytest

from mazes import Cell

def test_cell():
    c = Cell(1,2)
    c2 = Cell(1,3)

    assert c._row == 1
    assert c._column == 2
    assert len(c.links) == 0

    c.link(c2)
    assert c2 in c.links

    c.unlink(c2)
    assert c2 not in c.links


