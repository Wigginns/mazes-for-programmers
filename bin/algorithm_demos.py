from algorithms import BinaryTree
from mazes import Grid

grid = Grid(15,15)
b_t = BinaryTree()
print(grid)
b_t.apply(grid)

# c = grid[1,1]
# print(c._links)
# print(grid[0,0].linked)

print(grid)