from mazesforprogrammers import Cell, Grid
import pprint


def main():
    g = Grid(4,4)

    c = g[2,2]
    g[2,2] = Cell(2,2)
    print(c)
    # print(repr(c.north))

    # c = g._getCell(4,4)

    # print(repr(c._north))
    print(g)

    pp = pprint.PrettyPrinter()
    pp.pprint(g.print_grid())


if __name__ == "__main__":
    main()