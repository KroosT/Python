import os
import tempfile


def sort(filename, output, numbers = False, reverse=False, field_sep='\t',
         str_sep = '\n', buf_size = 1024 * 1024, checked = False):

    if checked:
        output_file = None
        input_file = open(output, 'r')
        count = os.path.getsize(output) // buf_size
    else:
        output_file = open(output, 'w')
        input_file = open(filename, 'r')
        count = os.path.getsize(filename) // buf_size

    files = []

    if os.path.getsize(filename) % buf_size != 0:
        count += 1

    data = ''
    for i in range(count):
        files.append(tempfile.NamedTemporaryFile())
        data


def dividing(data, filename, size, buf_size, str_sep, output):
    data += filename.read(size)
    data_to_next = ''
    if data[-len(str_sep):] != str_sep:
        if data != '' and data.rfind(str_sep) == -1:
            if size == buf_size:
                os.remove(output)
            raise MemoryError
        data_to_next = data[data.rfind(str_sep) + 1:]
        data = data[:data.rfind(str_sep)]
    return data, data_to_next
