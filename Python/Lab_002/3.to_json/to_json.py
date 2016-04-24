def to_json(obj, raise_unknown=False):
    string = ""
    count = 0
    if type(obj) == type({}):
        string += "{"
        for element in obj:
            count += 1
            string += to_json(element, raise_unknown)
            if count != len(obj):
                string += ", "
        return string + "}"

    elif type(obj) == type([]):
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
        string += '"' + obj + '"'
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
lst = [1, {"a": 1}, 5, "434", 'ewe', [{"fsd": "fd"}]]
print to_json(lst)
