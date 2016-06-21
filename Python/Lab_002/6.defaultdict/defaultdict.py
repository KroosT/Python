class DefaultDict(dict):
    def __getitem__(self, item):
        try:
            return super(DefaultDict, self).__getitem__(item)
        except KeyError:
            self[item] = DefaultDict()
            return self[item]


def main():
    x = DefaultDict()
    x["4:{3:5}"][4][3] = 5
    x[10][1] = 9
    x[10][2] = 4
    x[10][3] = "a"
    x[4] = "b"
    print x

if __name__ == '__main__':
    main()
