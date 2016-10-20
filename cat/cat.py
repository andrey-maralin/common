from sys import stdout


def cat(*args):
    line_number = 0
    for file_name in args:
        try:
            with open(file_name, 'r') as f:
                for line in f:
                    line_number += 1
                    stdout.write(line)
        except IOError:
            print "File {0} wasn't found!".format(file_name)
            continue
    return line_number


if __name__ == "__main__":
    print "\nLines number: {0}".format(cat('1.txt', '2.css'))
