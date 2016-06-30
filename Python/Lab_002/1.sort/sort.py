import argparse
import sys
import os
import tempfile


def main(argv):
    args = parse_args(argv)
    sort = FileSort(args)
    sort.lets_sort_it()


class FileSort:

    def __init__(self, args):
        self.args = args
        self.templist = []
        self.filename = '../file_generating/generated.txt'

    def split(self, bufsize=8192, line_separator='\n'):
        count = os.path.getsize(self.filename) / bufsize + 1
        print count

        with open(self.filename, "r") as unsortedfile:
            offset = 0
            for i in xrange(count):
                symbols_to_end_line = 0
                tempfilename = tempfile.mktemp()
                self.templist.append(tempfilename)

                unsortedfile.seek(offset + bufsize)
                while True:
                    char = unsortedfile.read(1)
                    symbols_to_end_line += 1
                    if char == line_separator or char == "":
                        break

                with open(tempfilename, "w") as temp:
                    unsortedfile.seek(offset)
                    temp.write(unsortedfile.read(bufsize + symbols_to_end_line))
                    offset += bufsize + symbols_to_end_line

    @staticmethod
    def cmp_lines(fieldseparator='\t', numeric=False, keys=None,
                  reverse=False):
        if reverse:
            def compare_lines(curr_line="", next_line=""):
                if curr_line == "" or next_line == "":
                    return False
                curr_line_fields = str(curr_line).split(fieldseparator)
                print curr_line_fields
                next_line_fields = str(next_line).split(fieldseparator)
                print next_line_fields

                if keys:
                    if numeric:
                        first = [int(curr_line_fields[key]) for key in keys]
                        second = [int(next_line_fields[key]) for key in keys]
                        return first >= second
                    else:
                        first = [curr_line_fields[key] for key in keys]
                        second = [next_line_fields[key] for key in keys]
                        return first >= second
                else:
                    if numeric:
                        first = [int(item) for item in curr_line_fields]
                        second = [int(item) for item in next_line_fields]
                        return first >= second
                    else:
                        return curr_line_fields >= next_line_fields
            return compare_lines
        else:
            def compare_lines(curr_line="", next_line=""):
                if curr_line == "" or next_line == "":
                    return False
                curr_line_fields = str(curr_line).split(fieldseparator)
                next_line_fields = str(next_line).split(fieldseparator)

                if keys:
                    if numeric:
                        first = [int(curr_line_fields[key]) for key in keys]
                        second = [int(next_line_fields[key]) for key in keys]
                        return first <= second
                    else:
                        first = [curr_line_fields[key] for key in keys]
                        second = [next_line_fields[key] for key in keys]
                        return first <= second
                else:
                    if numeric:
                        first = [int(item) for item in curr_line_fields]
                        second = [int(item) for item in next_line_fields]
                        return first <= second
                    else:
                        return curr_line_fields <= next_line_fields
            return compare_lines

    def tempfilesort(self, tempname, lineseparator='\n', fieldseparator='\t',
                     keys=None, numeric=False, reverse=False):
        with open(tempname, "r") as temp_file:
            lines = temp_file.read().split(lineseparator)
        sortedlines = self.sort(lines, fieldseparator, keys, numeric, reverse)

        with open(tempname, "w") as temp_file:
            for line in sortedlines:
                if line != "":
                    temp_file.write(line + lineseparator)

    def sort(self, lines, fieldseparator='\t', keys=None,
             numeric=False, reverse=False):

        if len(lines) <= 1:
            return lines

        left = lines[:len(lines)/2]
        right = lines[len(lines)/2:]

        return self.merge(self.sort(left, fieldseparator, keys, numeric,
                                    reverse),
                          self.sort(right, fieldseparator, keys, numeric,
                                    reverse),
                          fieldseparator, keys, numeric, reverse)

    def merge(self, left, right, fieldseparator='\t', keys=None, numeric=False,
              reverse=False):

        res, left_ind, right_ind = [], 0, 0
        compare_lines = self.cmp_lines(fieldseparator, numeric, keys, reverse)

        while left_ind < len(left) and right_ind < len(right):
            if compare_lines(left[left_ind], right[right_ind]):
                res.append(left[left_ind])
                left_ind += 1
            else:
                res.append(right[right_ind])
                right_ind += 1

        if left_ind >= len(left):
            res.extend(right[right_ind:])
        elif right_ind >= len(right):
            res.extend(left[left_ind:])

        return res

    def mergefiles(self, res_file, lineseparator, fieldseparator,
                   keys, numeric, reverse):

        templist = self.templist
        compare_lines = self.cmp_lines(fieldseparator, numeric, keys, reverse)
        with open(templist.pop(0), "r") as firstTemp:
            with open(templist.pop(0), "r") as secondTemp:
                if len(templist) == 0:
                    temp_name = res_file
                else:
                    temp_name = tempfile.mktemp()

                with open(temp_name, "w") as t_file:

                    firsttempstring = self.readline(firstTemp, lineseparator)
                    secondtempstring = self.readline(secondTemp, lineseparator)

                    while firsttempstring != "" and secondtempstring != "":
                        if compare_lines(firsttempstring, secondtempstring):
                            t_file.write(firsttempstring)
                            firsttempstring = self.readline(firstTemp,
                                                            lineseparator)
                        else:
                            t_file.write(secondtempstring)
                            secondtempstring = self.readline(secondTemp,
                                                             lineseparator)

                    if firsttempstring == "":
                        while secondtempstring != "":
                            t_file.write(secondtempstring)
                            secondtempstring = self.readline(secondTemp,
                                                             lineseparator)
                    elif secondtempstring == "":
                        while firsttempstring != "":
                            t_file.write(firsttempstring)
                            firsttempstring = self.readline(firstTemp,
                                                            lineseparator)
                templist.append(temp_name)

    @staticmethod
    def readline(filename, lineseparator='\n'):
        templist = []
        while True:
            char = filename.read(1)
            templist.append(char)
            if char == lineseparator or char == "":
                break
        return "".join(templist)

    @staticmethod
    def readnextline(filename, lineseparator='\n'):
        templist = []
        pos = filename.tell()
        while True:
            char = filename.read(1)
            templist.append(char)
            if char == lineseparator or char == "":
                break
        filename.seek(pos)
        return "".join(templist)

    def check_file(self, lineseparator='\n', fieldseparator='\t', numeric=False,
                   keys=None, reverse=False):
        with open(self.filename, "r") as checking:
            while True:
                currentline = self.readline(checking, lineseparator)
                nextline = self.readnextline(checking, lineseparator)
                if nextline == "":
                    return True
                if not self.cmp_lines(fieldseparator, numeric, keys,
                                      reverse)(currentline, nextline):
                    return False

    def lets_sort_it(self):
        if self.args.check:
            print self.check_file(self.args.lineseparator,
                                  self.args.fieldseparator, self.args.numeric,
                                  self.args.keys, self.args.reverse)
        else:
            self.split(self.args.bufsize, self.args.lineseparator)
            for temp_file in self.templist:
                self.tempfilesort(temp_file, self.args.lineseparator,
                                  self.args.fieldseparator, self.args.keys,
                                  self.args.numeric, self.args.reverse)
            while len(self.templist) > 1:
                self.mergefiles(self.args.output, self.args.lineseparator,
                                self.args.fieldseparator, self.args.keys,
                                self.args.numeric, self.args.reverse)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str)
    parser.add_argument('-o', '--output', type=str)
    parser.add_argument('-c', '--check', action='store_true')
    parser.add_argument('-n', '--numeric', action='store_true')
    parser.add_argument('-r', '--reverse', action='store_true')
    parser.add_argument('-l', '--lineseparator', type=str, default='\n')
    parser.add_argument('-f', '--fieldseparator', type=str, default='\t')
    parser.add_argument('-k', '--keys', type=int, nargs='+')
    parser.add_argument('--bufsize', type=int, default=4096)
    args = parser.parse_args(argv)
    return args

if __name__ == "__main__":
    main(sys.argv[1:])
