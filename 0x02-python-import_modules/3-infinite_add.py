#!/usr/bin/python3
# Prints the result of the addition of all arguments

if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    sum = 0
    for i in range(count - 1):
        sum += int(sys.argv[i + 1])

    print('{}'.format(int(sum)))
