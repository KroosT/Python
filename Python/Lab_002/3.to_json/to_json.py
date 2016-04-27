def to_json(obj, raise_unknown=False):
    string = ""
    count = 0
    if isinstance(obj, dict):
        string += "{"
        for element in obj:
            count += 1
            string += to_json(element, raise_unknown)
            if count != len(obj):
                string += ", "
        return string + "}"

    elif isinstance(obj, list) or isinstance(obj, tuple):
        string += "["
        for element in obj:
            count += 1
            string += to_json(element, raise_unknown)
            if count != len(obj):
                string += ", "
        return string + "]"

    elif type(obj) == int or type(obj) == float or type(obj) == long:
        string += str(obj)
        return string

    elif type(obj) == str or type(obj) == unicode:
        string += '"'
        for o in obj:
            if o == '"':
                string += "\\"
            string += o
        return string

    elif obj is True:
        return "true"

    elif obj is False:
        return "false"

    elif obj is None:
        return "null"

    else:
        if raise_unknown:
            raise TypeErrorException("Cannot convert an unknown type: ", obj)


class TypeErrorException(TypeError):

    def __init__(self, value, obj):
        super(TypeErrorException, self).__init__()
        self.value = value
        self.objType = type(obj)

    def __str__(self):
        return repr(self.value) + repr(self.objType)


class Unknown(object):
    def __init__(self):
        super(Unknown, self).__init__()
        self.a = 3

x = Unknown()
lst = [1, {"a": 1}, 5, "434", 'ew"e', [{"fsd": "fd"}, (1, 3)]]
print to_json(lst)
