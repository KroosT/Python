# Metaclass
def wrap(path):
    class MyMetaClass(type):
        def __new__(mcs, name, bases, dct):
            f = open(path, 'r')
            for line in f:
                values = line.split()
                dct[values[0]] = eval(values[2])
            return super(MyMetaClass, mcs).__new__(mcs, name, bases, dct)
    return MyMetaClass


class NewClass:
    def __init__(self):
        pass
    __metaclass__ = wrap('/home/kroos/Python/Lab_002/7.metaclass/test_err')


c = NewClass()
print c.number1
