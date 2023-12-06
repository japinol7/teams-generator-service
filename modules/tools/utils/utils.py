def read_file_as_string(file_name):
    res = []
    with open(file_name, "r", encoding='utf-8') as in_file:
        for line_in in in_file:
            res.append(line_in)
    return ''.join(res)


def write_string_to_file(file_name, string):
    with open(file_name, "w", encoding='utf-8') as out_file:
        out_file.write(string)
