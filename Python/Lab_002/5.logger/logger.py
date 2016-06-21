# Class logger with the possibility of inheritance. The class can save what
# methods and with what arguments was called and what was the result of it's
# call.


class Logger(object):
    log = str()

    def __getattribute__(self, item):
        obj = object.__getattribute__(self, item)

        def testfunc(*args):
            res = obj(*args)
            Logger.log += "Called '{0}' function with args {1}, result: {2}\n"\
                .format(item, args, res)
            return res

        if callable(obj):
            return testfunc

        return object.__getattribute__(self, item)

    def __str__(self):
        return Logger.log


class Test(Logger):

    def __init__(self):
        self.k = 2

    def multiply(self, x, y):
        return self.k * x * y

    def add(self, x):
        return self.k + x


def test():

    t = Test()
    t.add(4)
    t.multiply(5, 2)
    print str(t)


def main():
    test()

if __name__ == '__main__':
    main()
