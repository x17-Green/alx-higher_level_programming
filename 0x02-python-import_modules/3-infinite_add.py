#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    ans: int = 0

    for arg in argv[1:]:
        ans += int(arg)
    print("{:d}".format(ans))
