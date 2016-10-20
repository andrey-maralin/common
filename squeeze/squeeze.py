def squeeze(seq):
    seq = iter(seq)
    prev_elem = None
    for i in seq:
        if i != prev_elem:
            prev_elem = i
            yield i
        else:
            continue


if __name__ == "__main__":
    print list(squeeze([1, 2, 2, 100, 0, 0, 5]))
    print list(squeeze((2, 4, 5, 5, 5, 6, 7, 7, 5, 2, 4)))
    print list(squeeze(()))
