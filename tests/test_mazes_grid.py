import pytest

from mazesforprogrammers import Cell, Grid
from mazesforprogrammers.base.cell import is_cell
from mazesforprogrammers.base.grid import is_key

ROWS, COLUMNS = 6,7

def test_grid():
    with pytest.raises(ValueError):
        g = Grid(1,1)

    g = Grid(ROWS, COLUMNS)

    assert g.rows == ROWS
    assert g.columns == COLUMNS

    # TODO: Test configure_cells and prepare grid
    # test_grid_cell_neighbors() does some configure_cells testing

def test_grid_get_cell_at():
    g = Grid(ROWS, COLUMNS)

    c = g.cell_at(ROWS-2, COLUMNS-2)
    c2 = g[ROWS-2, COLUMNS-2]
    assert c == c2

    assert g[ROWS+1,COLUMNS+1] is None
    with pytest.raises(IndexError):
        g[1,2,3]

def test_grid_is_key():
    assert is_key((1,2))
    assert not is_key((1,2,3))
    assert not is_key((8.9,1.1))

def test_grid_set_cell_at():
    g = Grid(ROWS, COLUMNS)

    # TODO: set_cell_at test, happy path
    out_of_range_cell = Cell(15,15)
    with pytest.raises(IndexError):
        g[ROWS,COLUMNS] = out_of_range_cell
    with pytest.raises(ValueError):
        g[1,1] = 12

def test_grid_index_is_in_range():
    g = Grid(ROWS, COLUMNS)

    for r in range(ROWS):
        for c in range(COLUMNS):
            assert g.index_is_in_range((r,c))

    assert not g.index_is_in_range((-1,-1))
    assert not g.index_is_in_range((ROWS,COLUMNS))

def test_grid_random_cell():
    g = Grid(ROWS, COLUMNS)
    random_cell = g.random_cell()

    assert is_cell(random_cell)
    assert random_cell.row < ROWS and random_cell.column < COLUMNS

    for _ in range(33):
        random_cell = g.random_cell()
        assert random_cell.row < ROWS and random_cell.column < COLUMNS

def test_grid_cell_neighbors():
    g = Grid(ROWS, COLUMNS)
    c = g.cell_at(2, 2)

    assert c.north.row == 1 and c.north.column == 2
    assert c.south.row == 3 and c.south.column == 2

    assert c.east.row == 2 and c.east.column == 3
    assert c.west.row == 2 and c.west.column == 1


def test_grid_generators():
    g = Grid(ROWS, COLUMNS)
    generator_items = 0
    generator_rows = 0
    total_expected_items = ROWS * COLUMNS

    for _ in g.each_cell():
        generator_items += 1
    assert generator_items == total_expected_items

    for _ in g.each_row():
        generator_rows += 1
    assert generator_rows == ROWS

    # TODO: Test to ensure we get all items we expect
    # Might need to override __eq__ to do it easily?
    # all_cells = [
    #     Cell(0, 0), Cell(0, 1), Cell(0, 2), Cell(0, 3), Cell(0, 4), Cell(0, 5), Cell(0, 6),
    #     Cell(1, 0), Cell(1, 1), Cell(1, 2), Cell(1, 3), Cell(1, 4), Cell(1, 5), Cell(1, 6),
    #     Cell(2, 0), Cell(2, 1), Cell(2, 2), Cell(2, 3), Cell(2, 4), Cell(2, 5), Cell(2, 6),
    #     Cell(3, 0), Cell(3, 1), Cell(3, 2), Cell(3, 3), Cell(3, 4), Cell(3, 5), Cell(3, 6),
    #     Cell(4, 0), Cell(4, 1), Cell(4, 2), Cell(4, 3), Cell(4, 4), Cell(4, 5), Cell(4, 6),
    #     Cell(5, 0), Cell(5, 1), Cell(5, 2), Cell(5, 3), Cell(5, 4), Cell(5, 5), Cell(5, 6)
    # ]
    # assert g[1,1] in all_cells