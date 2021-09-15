import pytest

from mazes import Grid
from mazes.grid import is_key

def test_grid():
    with pytest.raises(ValueError):
        g = Grid(1,1)

    g = Grid(6,7)

    assert g._rows == 6
    assert g._columns == 7

    c = g.cell_at(4,4)
    c2 = g[4,4]
    assert c == c2

    assert is_key((1,2))
    assert not is_key((1,2,3)) 