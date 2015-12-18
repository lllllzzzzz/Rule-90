#!/usr/bin/python
 
import sys
 
def rule90(config, generations):
    """Print N generations of Rule 90 with initial cell configuration."""
   
    for generation in xrange(0, generations):
        printGeneration(config)
 
        next_config = ""
        cells = [int(i) for i in config]
 
        for i in xrange(0, len(cells)):
            if len(config) == 1:
                next_config += "0"
            elif i == 0:
                next_config += str(0 ^ int(cells[i + 1]))
            elif i == len(cells) - 1:
                next_config += str(int(cells[i - 1]) ^ 0)
            else:
                next_config += str(cells[i - 1] ^ cells[i + 1])
 
        config = next_config
 
def printGeneration(config):
    """Print generation of automaton given a configuration."""
 
    config = str.replace(config, "0", " ")
    config = str.replace(config, "1", "*")
    print config
 
def sierpinski(width, generations):
    """Print N generations of the Sierpinski Triangle."""
 
    zeroes = "".join(["0" for i in xrange(0, width / 2)])
    initial_config = zeroes + "1" + zeroes
    rule90(initial_config, generations)
 
def main():
    if len(sys.argv) != 3 or not (sys.argv[1] + sys.argv[2]).isdigit():
        print "Usage:", sys.argv[0], "[width] [generations]"
        sys.exit(0)
 
    sierpinski(int(sys.argv[1]), int(sys.argv[2]))
 
if __name__ == "__main__":
    main()
