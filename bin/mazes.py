from src.mazes import Cell, Grid


def main():
    g = Grid(4,4)

    c = g[2,2]
    g[2,2] = Cell(2,2)

    print(repr(c.north))

    # c = g._getCell(4,4)

    # print(repr(c._north))


if __name__ == "__main__":
    main()