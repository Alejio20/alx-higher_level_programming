#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv
    if len(arg) == 1:
        print('0 arguments.')
    elif len(arg) == 2:
        print('1 argument:')
    elif len(arg) > 2:
        print('{:d} arguments:'.format(len(arg)))
    i = 1
    for n in arg:
        print('{:d}: {:s}'.format(i, arg[i]))
        i += 1
