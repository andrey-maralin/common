
def squeeze(seq):
    prev_elem = seq[0]
    yield prev_elem
    for i in seq[1:]:
        if i != prev_elem:
            prev_elem = i
            yield i
        else:
            continue

if __name__ == "__main__":
    print list(squeeze([1, 2, 2, 100, 0, 0, 5]))
    print list(squeeze([0, 1, 1, 1, 3, 1, ]))
