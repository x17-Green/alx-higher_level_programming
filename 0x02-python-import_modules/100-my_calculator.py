#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    opr = (argv[2])
    b = int(argv[3])

    if opr == "+":
        result = add(a, b)
    elif opr == "-":
        result = sub(a, b)
    elif opr == "*":
        result = mul(a, b)
    elif opr == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, opr, b, result))
