# coding: utf8

#
# Remove the duplicate line of a file
#
import sys

def remove_duplicate_line(filename):
    exist_lines = list()

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue

            if line not in exist_lines:
                exist_lines.append(line)
                print(line)


if __name__ == "__main__":
    if (not sys.argv) or (len(sys.argv) != 2):
        print("Usage: python %s <file> " % __file__)
        sys.exit(1)
    
    filename = sys.argv[1]
    remove_duplicate_line(filename)
