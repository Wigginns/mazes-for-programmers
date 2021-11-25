from mazesforprogrammers import Cell
from mazesforprogrammers.base.cell import is_cell


def test_cell_init_and_helpers():
    c = Cell(1, 2)

    assert c._row == 1
    assert c._column == 2
    assert len(c.links) == 0

    assert str(c) == 'Cell row is 1 and column is 2.'
    assert repr(c) == 'Cell(row=1, column=2)'

    assert is_cell(c)
    assert not is_cell("I'm a sentence.")


def test_cell_linking_and_neighbors():
    middle_cell = Cell(2, 2)
    north_cell = Cell(1, 2)
    east_cell = Cell(2, 3)
    # south_cell = Cell(3, 2)
    # west_cell = Cell(2, 1)

    middle_cell.link(north_cell)
    middle_cell.link(east_cell)
    assert middle_cell.linked(east_cell)
    assert middle_cell.linked(north_cell)

    middle_cell.unlink(east_cell)
    assert not middle_cell.linked(east_cell)
    assert not east_cell.linked(north_cell)

    middle_cell.east = east_cell
    assert east_cell in middle_cell.neighbors
    assert repr(middle_cell.east) == "Cell(row=2, column=3)"
    assert Cell(4, 4) not in middle_cell.neighbors
