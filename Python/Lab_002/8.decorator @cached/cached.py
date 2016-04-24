def cached(function):

    def wrapper(*args):
        wrapper.previous_args = ""
        try:
            wrapper.count += 1
        except AttributeError:
            wrapper.count = 1
            wrapper.dict = {}

        for i in range(len(args)):
            wrapper.previous_args += str(args[i])
        if wrapper.previous_args in wrapper.dict:
            return wrapper.dict[wrapper.previous_args]
        else:
            result = function(*args)
            wrapper.dict[wrapper.previous_args] = result
            return result
    return wrapper


@cached
def union(*args):
    string = "{"
    for i in range(len(args)):
        string += str(args[i])
        if i != len(args) - 1:
            string += ", "
    string += "}"
    return string

print union(0, 1, 3, [1, 3])
print union(0, 1, 3, [1, 3])
print union(0, 1, 2)
