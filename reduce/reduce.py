def count_lines():
    file_name = "big_file.txt"
    with open(file_name, "r") as f:
        return reduce(lambda a, _: a+1, f, 0)

if __name__ == "__main__":

    print count_lines()