import math


class NVector(object):

    def __init__(self, *args):
        self.len = 0
        self.sum = 0
        self.lst = []
        for a in args:
            self.lst.append(a)

    def __add__(self, other):
        v = NVector()
        if len(self.lst) < len(other):
            for i in range(len(self.lst)):
                v.push(self.lst[i] + other[i])
            for i in range(len(self.lst), len(other)):
                v.push(self.lst[i])
        elif len(self.lst) > len(other):
            for i in range(len(other)):
                v.push(self.lst[i] + other[i])
            for i in range(len(other), len(self.lst)):
                v.push(self.lst[i])
        else:
            for i in range(len(self.lst)):
                v.push(self.lst[i] + other[i])
        return v

    def __sub__(self, other):
        v = NVector()

        if len(self.lst) < len(other):
            for i in range(len(self.lst)):
                v.push(self.lst[i] - other[i])
            for i in range(len(self.lst), len(other)):
                v.push(self.lst[i])
        elif len(self.lst) > len(other):
            for i in range(len(other)):
                v.push(self.lst[i] - other[i])
            for i in range(len(other), len(self.lst)):
                v.push(self.lst[i])
        else:
            for i in range(len(self.lst)):
                v.push(self.lst[i] - other[i])
        return v

    def __mul__(self, other):
        v = NVector()

        if type(other) != type(self):
            for i in range(len(self.lst)):
                v.push(self.lst[i] * other)
        else:
            for i in range(len(self.lst)):
                v.push(self.lst[i] * other[i])
        return v

    def __eq__(self, other):

        if len(self.lst) != len(other):
            return False
        else:
            for i in range(len(self.lst)):
                if self.lst[i] != other[i]:
                    return False
        return True

    def __ne__(self, other):

        if len(self.lst) != len(other):
            return True
        else:
            for i in range(len(self.lst)):
                if self.lst[i] != other[i]:
                    return True
        return False

    def length(self):
        for i in range(len(self.lst)):
            self.sum += pow(self.lst[i], 2)
        self.len = math.sqrt(self.sum)
        return self.len

    def __str__(self):
        self.string = "{"
        for i in range(len(self.lst)):
            self.string += str(self.lst[i])
            if i != len(self.lst) - 1:
                self.string += ", "
        self.string += "}"
        return self.string

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, item):
        return self.lst[item]

    def push(self, value):
        self.lst.append(value)


v1 = NVector(0, 1, 2, 3)
v2 = NVector(0, 1, 2, 3)
v3 = NVector(0, 1, 1)
v4 = NVector(0, 0, 1)

print v1 + v3
print v1 * v2
print v3 == v4
print v3 != v1
print v1[2]
print v1 * 3
