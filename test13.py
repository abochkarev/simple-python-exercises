from common import show


@show
def max_in_list(list_=None):
    if not list_:
        raise RuntimeError("List shouldn't be none or empty.")
    max_ = list_[0]
    for i in xrange(1, len(list_)):
        if list_[i] > max_:
            max_ = list_[i]
    return max_


assert max_in_list([1, 2, 3, 4, 5, 6]) == 6
assert not max_in_list([1, 2, 3, 4, 5, 76]) == 1

