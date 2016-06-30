def cached(function):

    def wrapper(*args):

        try:
            if str(args) in wrapper.previous_args_dict:
                print 'Same args detected'
                return wrapper.previous_args_dict[str(args)]
            else:
                wrapper.previous_args_dict[str(args)] = function(*args)
                return wrapper.previous_args_dict[str(args)]
        except AttributeError:
            wrapper.previous_args_dict = {str(args): function(*args)}
            return wrapper.previous_args_dict[str(args)]
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


def main():
    print union(0, 1, 3, [1, 3])
    print union(0, 1, 3, [1, 3])
    print union(0, 1, 2)
    print union(0, 1, 2)

if __name__ == '__main__':
    main()
