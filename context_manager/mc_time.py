import time

class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print time.time() - self.start


def big_list(num_of_elements=1000000, element=50000):
    return range(num_of_elements)[element]

if __name__ == "__main__":

    with Timer():
        print big_list()

    with Timer():
        print big_list(element=50)
