#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ans = 0

    if len(argv) == 1:
        print("Error: input an int: {:d}".format(len(argv) - 1))
    else:
        for arg in argv[1:]:
            ans += int(arg)
        print("Total sum is = {}".format(ans))
