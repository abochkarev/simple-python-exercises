from common import show


@show
def max(a, b):
    return a if a >= b else b


assert max(1, 3) == 3
assert max(3, 1) == 3
assert max(2, 2) == 2
