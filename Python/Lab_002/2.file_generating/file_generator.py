import random
import string
import argparse


def file_generator(field_count, bool_numeric, field_sep, str_sep, str_count):
    _str = 0
    with open('generated.txt', 'w') as f:
        while _str != str_count:
            _field = 0
            while _field != field_count:
                if bool_numeric:
                    f.write(''.join(random.choice(string.digits)
                                    for _ in range(6)))
                else:
                    f.write(''.join(random.choice(string.ascii_uppercase +
                                                  string.ascii_lowercase)
                                    for _ in range(6)))
                if _field != field_count - 1:
                    f.write(field_sep)
                _field += 1
            if str != str_count - 1:
                f.write(str_sep)
            _str += 1

parser = argparse.ArgumentParser()
parser.add_argument('-sc', '--str_count', type=int, default=5,
                    help='Count of strings in the generated file')
parser.add_argument('-fc', '--field_count', type=int, default=5,
                    help='Count of fields in the generated file')
parser.add_argument('-ss', '--str_sep', type=str, default='\n',
                    help='String separator')
parser.add_argument('-fs', '--field_sep', type=str, default='\t',
                    help='Field separator')
parser.add_argument('-n', '--numeric', action='store_true', default=False,
                    help='Field as numbers')
args = parser.parse_args()
file_generator(args.field_count, args.numeric, args.field_sep,
               args.str_sep, args.str_count)
