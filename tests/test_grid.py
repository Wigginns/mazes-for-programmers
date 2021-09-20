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


def test_grid_generators():
    rows = 6
    columns = 7
    grid = Grid(rows,columns)
    generator_items = 0
    generator_rows = 0
    total_expected_items = rows * columns

    for _ in grid.each_cell():
        generator_items += 1
    assert generator_items == total_expected_items

    for _ in grid.each_row():
        generator_rows += 1
    assert generator_rows == rows