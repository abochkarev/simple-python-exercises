from common import show


@show
def map_(func, list_):
    return [func(x) for x in list_]


@show
def filter(func, list_):
    return [x for x in list_ if func(x)]


assert map_(str, [1, 2, 3, 4, 5]) == ["1", "2", "3", "4", "5"]
assert filter(lambda x: x > 4, [1, 2, 3, 4, 5]) == [5]
