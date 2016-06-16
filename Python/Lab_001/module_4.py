from __future__ import print_function
import sys
import argparse


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('num', type=int, help='print num of fibonacci '
                                              'numbers')
    return parser.parse_args(args)


def fibonacci(_n):

    counter, first, second = 0, 0, 1
    while counter < _n:
        yield first
        first, second = second, first + second
        counter += 1


def main(argv):
    args = parse_args(argv)
    n = args.num
    for num in fibonacci(n):
        print (num, end=' ')

if __name__ == "__main__":
    main(sys.argv[1:])
