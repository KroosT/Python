class Filter(object):

    def __init__(self, args):
        self.object = [elem for elem in args]

    def __iter__(self):
        return iter(self.object)

    def __str__(self):
        return str(self.object)

    def deselect(self, function):
        for i in range(len(self.object)):
            if function(self.object[i]):
                yield self.object[i]


def even(number):

    if number % 2 == 0:
        return True
    else:
        return False


def main():
    a = Filter([5, 1, 2, 3, 4])
    print list(a.deselect(even))

if __name__ == '__main__':
    main()