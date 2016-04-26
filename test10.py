from common import show


@show
def overlapping(list1=None, list2=None):
    for x in list1 or []:
        for y in list2 or []:
            if x == y:
                return True
    return False

assert overlapping([1, 2, 3], [2, 3, 4])
assert not overlapping()
assert not overlapping([1, 2, 3], [4, 5, 6])

