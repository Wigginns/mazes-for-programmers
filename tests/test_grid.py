import pytest
from typing import List

from mazes import Cell
from mazes.cell import is_cell
from mazes import Grid
from mazes.grid import is_key, CellList

def test_grid():
    with pytest.raises(ValueError):
        g = Grid(1,1)

    ROWS, COLUMNS = 6,7

    g = Grid(ROWS, COLUMNS)

    # TODO: Test configure_cells and prepare grid

    assert g.rows == ROWS
    assert g.columns == COLUMNS

    for r in range(ROWS):
        for c in range(COLUMNS):
            assert g.index_is_in_range((r,c))

    assert not g.index_is_in_range((-1,-1))
    assert not g.index_is_in_range((ROWS,COLUMNS))

    # Test cell retrieval
    c = g.cell_at(4,4)
    c2 = g[4,4]
    assert c == c2

    assert is_key((1,2))
    assert not is_key((1,2,3))
    assert not is_key((8.9,1.1))


    assert g[ROWS+1,COLUMNS+1] is None
    with pytest.raises(IndexError):
        g[1,2,3]

    random_cell = g.random_cell()
    assert is_cell(random_cell)
    assert random_cell.row < g.rows and random_cell.column < g.columns

    # TODO: set_cell_at test, happy path
    out_of_range_cell = Cell(15,15)
    with pytest.raises(IndexError):
        g[ROWS,COLUMNS] = out_of_range_cell
    with pytest.raises(ValueError):
        g[1,1] = 12

# TODO: Add tests for index checker

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