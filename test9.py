from common import show


@show
def is_member(x, list_=None):
    for a in list_ or []:
        if a == x:
            return True
    return False


assert is_member(1, [1, 1, 2, 3, 4, 2, 1])
assert not is_member('a', [1, 2, 3, 4])
assert is_member('a', ['b', 'a', 'c'])
assert not is_member(7, [1, 2, 3, 4, 5, 6])
assert not is_member(7)
