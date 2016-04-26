from common import show


@show
def sum(list_=None):
    sum_ = 0
    for i in list_ or []:
        sum_ += i
    return sum_


@show
def multiply(list_=None):
    if not list_:
        return 0
    multiply_ = 1
    for i in list_ or []:
        multiply_ *= i
    return multiply_


assert sum([1, 2, 3]) == 6
assert not sum([2, 2, 2]) == 7
assert sum() == 0
assert sum([1, 2, 3, 4]) == 10

assert multiply([1, 2, 3]) == 6
assert not multiply([2, 2, 2]) == 7
assert multiply([9, 9, 9]) == 729
assert multiply([1, 2, 3, 4]) == 24
assert multiply() == 0
