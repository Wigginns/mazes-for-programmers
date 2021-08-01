import pytest

from mazes import Grid

def test_grid():
    with pytest.raises(ValueError):
        g = Grid(1,1)

    g = Grid(6,7)

    assert g._rows == 6
    assert g._columns == 7
    c = g._getCell(4,4)

    c = g[4,4]

    print(repr(c.north))