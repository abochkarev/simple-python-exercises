from common import show


@show
def for_loop(list_):
    res_list_ = []
    for i in list_:
        res_list_.append(len(i))
    return res_list_


@show
def map_(list_):
    return map(len, list_)


@show
def list_comprehension(list_):
    return [len(i) for i in list_]


list_ = ["a", "bb", "ccc"]
assert for_loop(list_) == [1, 2, 3]
assert map_(list_) == [1, 2, 3]
assert list_comprehension(list_) == [1, 2, 3]
