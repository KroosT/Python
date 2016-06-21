# Own xrange()
class XRange(object):

    def __init__(self, *args):
        if len(args) == 1:
            start, stop, step = 0, args[0], 1
        elif len(args) == 2:
            start, stop, step = args[0], args[1], 1
        elif len(args) == 3:
            start, stop, step = args
        else:
            raise TypeError('xrange() requires 1-3 int arguments')

        try:
            start, stop, step = int(start), int(stop), int(step)
        except ValueError:
            raise TypeError('an integer is required')

        if step == 0:
            raise ValueError('xrange() arg 3 must not be zero')
        elif step < 0:
            stop = min(stop, start)
            last = max(stop, start)
            step_sign = -1
        else:
            stop = max(stop, start)
            last = min(stop, start)
            step_sign = 1

        self._start = start
        self._stop = stop
        self._step = step
        self._last = last - step
        self._step_sign = step_sign

    def __iter__(self):
        return self

    def next(self):
        self._last += self._step
        if self._step_sign > 0:
            if self._last >= self._stop:
                raise StopIteration()
        else:
            if self._last <= self._stop:
                raise StopIteration()
        return self._last


# Test our oun xrange()
def test_xrange():

    for x in XRange(5, 3, -1):
        print x


def main():
    test_xrange()

if __name__ == '__main__':
    main()
