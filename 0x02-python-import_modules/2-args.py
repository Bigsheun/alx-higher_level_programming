#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)

    print("{:d} argument".format(argv_count), end="")
    if argv_count == 0:
        print("s.")
    elif argv_count == 1:
        print(":")
    else:
        print("s:")

    index = 1
    while index <= argv_count:
        print("{:d}: {:s}".format(index, sys.argv[index]))
        index += 1
