"""making coordinates"""


def get_coords(xs: str, ys: str) -> None:
    index_xs = 0
    while index_xs < len(xs):
        index_ys = 0
        xcoords = "(" + xs[index_xs] + ","
        while index_ys < len(ys):
            both_coords = xcoords + ys[index_ys] + ")"
            print(both_coords)
            index_ys += 1
        index_xs += 1


get_coords("hi", "bye")
