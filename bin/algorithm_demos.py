from mazesforprogrammers import BinaryTree, Sidewinder
from mazesforprogrammers import Grid


def main():
    bt_grid = Grid(15,15)
    bt = BinaryTree()
    print(bt_grid)
    bt.apply(bt_grid)

    print(bt_grid)



    sw_grid = Grid(15,15)
    sw = Sidewinder()
    print(sw_grid)
    sw.apply(sw_grid)

    print(sw_grid)


if __name__ == "__main__":
    main()