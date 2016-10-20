from sys import stdout
result_file_name = 'result.txt'


def cat(*args):
    line_number = 0
    with stdout as out:
        for file_name in args:
            try:
                with open(file_name, 'r') as f:
                    for line in f:
                        line_number += 1
                        out.write(line)
                    out.write('\n')
            except IOError:
                print "File {0} wasn't found!".format(file_name)
                continue
        print
    return line_number


if __name__ == "__main__":
    cat('1.txt', '2.css')
