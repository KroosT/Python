import argparse
import sys


def parse_args(args):
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group()
    source.add_argument('-f', '--file', type=argparse.FileType('r'),
                        nargs='?', const='data.txt', help='get numbers from '
                                                          'FILE (default: '
                                                          'data.txt)')
    sort_kind = parser.add_mutually_exclusive_group()
    sort_kind.add_argument('-q', '--quick', action='store_const',
                           const='q', dest='sort',
                           help='quick sort (as default)')
    sort_kind.add_argument('-m', '--merge', action='store_const',
                           const='m', dest='sort', help='merge sort')
    sort_kind.add_argument('-r', '--radix', action='store_const',
                           const='r', dest='sort', help='radix sort')
    sort_kind.set_defaults(sort='q')
    source.set_defaults(file='data.txt')
    return parser.parse_args(args)


def quick_sort(lst, first, last):

    if first < last:
        split = partition(lst, first, last)
        quick_sort(lst, first, split - 1)
        quick_sort(lst, split + 1, last)


def partition(lst, start, end):

    pivot = lst[end]
    bottom = start-1
    top = end

    done = 0
    while not done:
        while not done:
            bottom += 1

            if bottom == top:
                done = 1
                break

            if lst[bottom] > pivot:
                lst[top] = lst[bottom]
                break

        while not done:
            top -= 1

            if top == bottom:
                done = 1
                break

            if lst[top] < pivot:
                lst[bottom] = lst[top]
                break

    lst[top] = pivot

    return top


def merge_sort(lst):

    if len(lst) > 1:
        mid = len(lst) // 2
        lm = lst[:mid]
        rm = lst[mid:]

        merge_sort(lm)
        merge_sort(rm)

        i = 0
        j = 0
        k = 0

        while i < len(lm) and j < len(rm):
            if lm[i] < rm[j]:
                lst[k] = lm[i]
                i += 1
            else:
                lst[k] = rm[j]
                j += 1
            k += 1

        while i < len(lm):
            lst[k] = lm[i]
            i += 1
            k += 1

        while j < len(rm):
            lst[k] = rm[j]
            j += 1
            k += 1

    return


def radix_sort(lst):

    rad = 10
    max_len = False
    placement = 1

    while not max_len:
        max_len = True
        buckets = [list() for _ in range(rad)]

        for i in lst:
            tmp = int(i) / placement
            buckets[tmp % rad].append(i)
            if max_len and tmp > 0:
                max_len = False

        a = 0
        for b in range(rad):
            buck = buckets[b]
            for i in buck:
                lst[a] = i
                a += 1

        placement *= rad


def main(argv):
    args = parse_args(argv)
    inp = []
    if args.file is not None:
        with args.file as myfile:
            for line in myfile:
                if len(line.split()) == 10:
                    inp = line.split()
                    break
                else:
                    inp = []
    # q_mas = q_inp.split()
    # m_mas = m_inp.split()
    # quick_sort(q_mas, 0, len(q_mas) - 1)
    # merge_sort(m_mas)
    if args.sort == 'q':
        quick_sort(inp, 0, len(inp) - 1)
    elif args.sort == 'm':
        merge_sort(inp)
    elif args.sort == 'r':
        radix_sort(inp)
    print inp

if __name__ == "__main__":
    main(sys.argv[1:])
