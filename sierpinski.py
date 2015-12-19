#!/usr/bin/python
 
import sys

def step(gen):
    """Return the next step of Rule 90 given a cell configuration."""

    return [gen[i - 1] ^ gen[i + 1] for i in xrange(1, len(gen) - 1)]

def rule90(gen, steps):
    """Print N generations of Rule 90 with initial cell configuration."""
   
    for i in xrange(0, steps):
        print_gen(gen[1:-1])
        gen = [0] + step(gen) + [0]

def print_gen(gen):
    """Print generation of automaton given a configuration."""

    print "".join(["*" if i == 1 else " " for i in gen])

def init_gen(width):
    """Return initial configuration of Sierpinski Triangle given a width."""

    return [int(i) for i in ("0" * (width / 2)) + "1" + ("0" * (width / 2))]

def sierpinski(width, steps):
    """Print N steps of the Sierpinski Triangle."""

    rule90(init_gen(width), steps)
 
def main():
    if len(sys.argv) != 3 or not (sys.argv[1] + sys.argv[2]).isdigit():
        print "Usage:", sys.argv[0], "[width] [steps]"
        sys.exit(0)
 
    width = int(sys.argv[1])
    steps = int(sys.argv[2])
    sierpinski(width, steps)
 
if __name__ == "__main__":
    main()
