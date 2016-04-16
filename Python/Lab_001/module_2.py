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


# q_inp = raw_input('Input list of numbers for QuickSort: ')
# m_inp = raw_input('Input list of numbers for MergeSort: ')
with open('data.txt', 'r') as myfile:
    for line in myfile:
        if len(line.split()) == 10:
            r_inp = line.split()
            break
        else:
            r_inp = []
# q_mas = q_inp.split()
# m_mas = m_inp.split()
# quick_sort(q_mas, 0, len(q_mas) - 1)
# merge_sort(m_mas)
radix_sort(r_inp)
# print q_mas
# print m_mas
print r_inp
