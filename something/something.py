from squeeze import squeeze


def do_something(seq, x, y):
    square = list(squeeze.squeeze(filter(lambda e: e**2 > x, seq)))
    cube = list(squeeze.squeeze(filter(lambda e: e**3 > y, seq)))
    return len(square) - len(cube)


if __name__ == "__main__":
    print do_something([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,31,4,222,42,24,24,2242],11,11)
    print do_something([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,31,4,222,42,24,24,2242],2,300)