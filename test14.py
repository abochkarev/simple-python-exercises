from common import show


@show
def maps(list_):
    return [len(x) for x in list_]


assert maps(["a", "b", "c"]) == [1, 1, 1]
assert maps(["ab", "bc", "cd"]) == [2, 2, 2]
assert not maps(["ab", "bc", "cd"]) == [1, 1, 1]
