from algorithms import BinaryTree
from mazes import Grid

grid = Grid(5,5)
b_t = BinaryTree()
b_t.apply(grid)

# c = grid[1,1]
# print(c._links)
# print(grid[0,0].linked)

print(grid)