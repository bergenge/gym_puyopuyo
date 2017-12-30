import sys


def print_color(color, bright=True, outfile=sys.stdout):
    if bright:
        outfile.write("\x1b[3{};1m".format(color))
    else:
        outfile.write("\x1b[3{}m".format(color))


def print_reset(outfile=sys.stdout):
    outfile.write("\x1b[0m")


def print_up(n, outfile=sys.stdout):
    for _ in range(n):
        outfile.write("\033[A")


def print_down(n, outfile=sys.stdout):
    for _ in range(n):
        outfile.write("\033[B")


def print_forward(n, outfile=sys.stdout):
    for _ in range(n):
        outfile.write("\033[C")


def print_back(n, outfile=sys.stdout):
    for _ in range(n):
        outfile.write("\033[D")