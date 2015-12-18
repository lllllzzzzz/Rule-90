#!/usr/bin/python
 
import sys
 
def rule90(config, steps):
    """Print N steps of Rule 90 with initial cell configuration."""
   
    for step in xrange(0, steps):
        next_config = ""
        print config
 
        for i in xrange(0, len(config)):
            if len(config) == 1:
                next_config += "0"
            elif i == 0:
                next_config += str(0 ^ int(config[i + 1]))
            elif i == len(config) - 1:
                next_config += str(int(config[i - 1]) ^ 0)
            else:
                next_config += str(int(config[i - 1]) ^ int(config[i + 1]))
        config = next_config
 
def main():
    if len(sys.argv) != 3 or not (sys.argv[1] + sys.argv[2]).isdigit():
        print "Usage:", sys.argv[0], "[configuration] [steps]"
        sys.exit(0)
 
    rule90(sys.argv[1], int(sys.argv[2]))
 
if __name__ == "__main__":
    main()
