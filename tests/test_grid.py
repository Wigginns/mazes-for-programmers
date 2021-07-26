import pytest

from mazes import Grid

def test_grid():
    g = Grid(6,7)

    assert g._rows == 6
    assert g._columns == 7
    c = g._getCell(4,4)

    print(repr(c._north))