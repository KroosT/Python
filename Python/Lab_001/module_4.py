from __future__ import print_function


def fibonacci(_n):

    counter, first, second = 0, 0, 1
    while counter < _n:
        yield first
        first, second = second, first + second
        counter += 1

n = input('Number: ')
for num in fibonacci(n):
    print (num, end=' ')
