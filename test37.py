def read_file(file_name):
    with open(file_name) as f:
        while True:
            data = f.readline()
            if not data:
                break
            yield data


def create_numbered_file(file_name):
    with open('numbered-%s' % file_name, mode='w') as f:
        line_number = 1
        for data in read_file(file_name):
            f.write("%s. %s" % (line_number, data))
            line_number += 1


create_numbered_file('palindromes.txt')
