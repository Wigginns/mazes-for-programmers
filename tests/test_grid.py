import pytest

from mazes.base.grid import Grid
from mazes.base.cell import is_cell

def test_grid():
    with pytest.raises(ValueError):
        g = Grid(1,1)

    g = Grid(6,7)

    assert g._rows == 6
    assert g._columns == 7

    c = g[4,4]

    assert is_cell(c)

    cc = g.random_cell()

    assert is_cell(cc)

    # print(repr(c.north))