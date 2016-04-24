# Metaclass
class MyMetaClass(type):
    def __new__(mcs, name, bases, dct):
        path = dct['path']
        f = open(path, 'r')
        for line in f:
            values = line.split()
            dct[values[0]] = eval(values[2])
        return super(MyMetaClass, mcs).__new__(mcs, name, bases, dct)


class NewClass:
    def __init__(self):
        pass
    __metaclass__ = MyMetaClass
    path = '/home/kroos/Python/Lab_002/7.metaclass/test_err'


c = NewClass()
print c.number1
