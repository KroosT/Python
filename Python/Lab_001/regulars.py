import argparse
import re
import sys


def parse_args(args):
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--email', help='validate e-mail address')
    group.add_argument('-f', '--float', help='validate float number')
    group.add_argument('-u', '--url', help='get parts of url address')
    return parser.parse_args(args)


def is_valid_email(email):
    email_rules = re.compile(r"""
        ^[\w!#$%&'*+\-/=?^_`{|}~]+
        (\.[\w!#$%&'*+\-/=?^_`{|}~]+)*@[\w\-_]+.[\w\-_]+$
        """, re.IGNORECASE | re.VERBOSE)
    return email_rules.match(email)


def is_valid_float(num):
    float_rules = re.compile(r"^(\d)+([.](\d)+)?$")
    return float_rules.match(num)


def parse_url(url):
    url_rules = re.compile(r"""
        ^(?P<scheme>[a-z][\w+.\-]*):
        (//
            (?P<authority>
                ((?P<user>[\w+.\-]+):(?P<password>[\w+.\-]+)@)?
                (?P<host>[\w+.\-]*(:(?P<port>[\d]){1,5})?)
            )
        )?
        (?P<path>(?(authority)/)[\w+.\-/%,]*)?
        (\?(?P<query>[\w+.\-]+))?
        (\#(?P<fragment>[\w+.\-]+))?$
        """, re.IGNORECASE | re.VERBOSE)
    parsed_url = url_rules.match(url)
    if parsed_url:
        return parsed_url.groupdict()
    else:
        return False


def main(argv):
    args = parse_args(argv)
    if args.email:
        if is_valid_email(args.email):
            print '%s is a valid email.' % args.email
        else:
            print '%s is not a valid email.' % args.email
    elif args.float:
        if is_valid_float(args.float):
            print '%s is a valid float.' % args.float
        else:
            print '%s is not a valid float.' % args.float
    elif args.url:
        parsed_url = parse_url(args.url)
        if not parsed_url:
            print 'Given url is not valid.'
        else:
            for key, value in parsed_url.iteritems():
                print key + ': ' + str(value)

if __name__ == "__main__":
    main(sys.argv[1:])
