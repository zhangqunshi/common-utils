# coding: utf8

#
# Output the given colum of a file
#
import sys

column_separator = ":"

def read_column(filename, idx):
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue

            columns = line.split(column_separator)
            if columns:
                print(columns[idx])


if __name__ == "__main__":
    if (not sys.argv) or (len(sys.argv) != 3):
        print("Usage: python %s <file> <columnIndex>" % __file__)
        sys.exit(1)
    
    filename = sys.argv[1]
    column_idx = int(sys.argv[2])
    # print("start to read file: %s" % filename)
    read_column(filename, column_idx)
