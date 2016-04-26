from common import show


@show
def reduce_(list_):
    return reduce(max, list_)


assert reduce_([1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 1]) == 7
assert not reduce_([1, 2, 3, 4, 5, 6, 7, 8, 6, 5, 4, 3, 1]) == 6