from random import choice

from .algorithm import Algorithm
from mazes import Grid
from mazes import Cell

class BinaryTree():
    """
    Uses a simple random selection algorithm to convert a given Grid into a binary tree.
    For each Cell in the Grid we choose north or east and link to it.
    The top row always chooses east, the east column always chooses north.
    Northeast cell will have no eligible neighbors
    """

    def apply(self, grid: Grid) -> None:
        for cell in grid.each_cell():
            neighbors = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)
            if neighbors:
                cell.link(choice(neighbors)) if len(neighbors) > 0 else cell.link(neighbors[0])
