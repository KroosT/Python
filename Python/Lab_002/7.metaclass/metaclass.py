# Initialize file path
def file_path():
    choice = raw_input("If you want to choose another file path, please type "
                       "'y': ")
    if choice == 'y':
        x = 0
        while x == 0:
            ans = raw_input("Type new path: ")
            try:
                _ = open(ans, 'r')
                for line in _:
                    a = line.split()
                    n = a[0]
                    v = a[2]
                _.close()
                return ans
            except IOError:
                print("Invalid file path")
            except IndexError:
                print("Invalid name or value of attribute")
    else:
        ans = "/home/kroos/Python/Lab_002/7.metaclass/attrs"
        return ans


# Metaclass
class MyMetaClass(type):
    def __call__(cls, *args):
        obj = type.__call__(cls, *args)
        path = file_path()
        f = open(path, 'r')
        for line in f:
            a = line.split()
            name = a[0]
            value = a[2]
            setattr(obj, name, value)
        return obj


class NewClass:
    def __init__(self):
        pass
    __metaclass__ = MyMetaClass


c = NewClass()
print c.number1
