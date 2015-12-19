#!/usr/bin/python
 
import sys
 
def step(gen):
    """Return the next step of Rule 90 given a cell configuration."""
 
    return [gen[i - 1] ^ gen[i + 1] for i in xrange(1, len(gen) - 1)]
 
def rule90(gen, steps):
    """Print N generations of Rule 90 with initial cell configuration."""
   
    for i in xrange(0, steps):
        print "".join([str(i) for i in gen[1:-1]])
        gen = [0] + step(gen) + [0]
 
def main():
    if len(sys.argv) != 3 or not (sys.argv[1] + sys.argv[2]).isdigit():
        print "Usage:", sys.argv[0], "[configuration] [steps]"
        sys.exit(-1)
 
    init_gen = [int(i) for i in sys.argv[1]]
    steps = int(sys.argv[2])
    rule90([0] + init_gen + [0], steps)
 
if __name__ == "__main__":
    main()
