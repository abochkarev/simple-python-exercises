from common import show


@show
def len_(list_=None):
    count = 0
    for _ in list_ or []:
        count += 1
    return count


assert len_([1, 2, 3, 4]) == 4
assert len_([2, 3, 4, 5]) == 4
assert len_() == 0
