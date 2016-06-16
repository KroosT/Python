import argparse
import sys


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), nargs='?',
                        const='data.txt', help='read text from FILE ('
                                               'default: text.txt)')
    parser.add_argument('-n', type=int, default=2, help='n in n-grams stats')
    parser.add_argument('-k', type=int, default=6, help='k in n-grams stats')
    parser.set_defaults(file='data.txt')
    return parser.parse_args(args)


def repeat_word_counter(t_lst):

    t_dct = dict()
    for word in t_lst:
        if word in t_dct:
            t_dct[word] += 1
        else:
            t_dct[word] = 0

    return t_dct


def average_number_of_words(a_lst, a_count):

    _counter = len(a_lst)
    _average = _counter / a_count

    return _average


def del_specials(d_lst):

    _count = 0
    number_of_words = []
    result = []
    new_lst = list()
    specials = [',', '!', '?', '(', ')', ':', ';', '"', '@', '<', '>', '.']
    number_of_words.append(0)
    k = 0
    for x in d_lst:
        number_of_words[k] += 1
        for j in specials:
            if x[len(x) - 1] == j:
                x = x[:-1]
                if j == '.' or j == '!' or j == '?':
                    _count += 1
                    number_of_words.append(0)
                    k += 1
        new_lst.append(x)
    number_of_words.remove(0)
    result.append(new_lst)
    result.append(_count)
    result.append(number_of_words)

    return result


def median_value(mas):

    mas.sort()
    c = len(mas)
    if c % 2 == 0:
        _result = (mas[c / 2 - 1] + mas[c / 2]) / 2.0
    else:
        _result = mas[c / 2]
    return _result


def n_grams(n_lst, n):

    d = dict()
    for w in n_lst:
        l = 0
        if len(w) >= n:
            for _ in w:
                if l < len(w) - n + 1:
                    gr = w[l:l+n]
                    if gr in d:
                        d[gr] += 1
                    else:
                        d[gr] = 0
                    l += 1

    return d


def sort_func(u_grams):

    s_grams = list(u_grams.items())
    s_grams.sort(key=lambda item: item[1])
    s_grams.reverse()

    return s_grams


def main(argv):
    args = parse_args(argv)
    string = ""
    if args.file is not None:
        with args.file as myfile:
            string = myfile.readline()
    lst = string.split()
    temp = del_specials(lst)
    lst = temp[0]
    count = temp[1]
    words_in_sentence = temp[2]
    average = average_number_of_words(lst, count)
    dct = repeat_word_counter(lst)
    median = median_value(words_in_sentence)
    grams = n_grams(lst, args.n)
    grams = sort_func(grams)
    keys = dct.keys()
    i = -1
    for value in dct:
        i += 1
        print 'Word "{}" repeats {} times'.format(keys[i], dct[value])
    print 'Average number of words is {} per sentence'.format(average)
    print 'Median number of words in sentence is {}'.format(median)
    print 'Top-{} the most repeated {}-grams: '.format(args.k, args.n)
    jt = -1
    for g in grams:
        jt += 1
        if jt <= args.k - 1:
            print '{}: {} - {}'.format(jt + 1, g[0], g[1])
        else:
            break

if __name__ == "__main__":
    main(sys.argv[1:])
