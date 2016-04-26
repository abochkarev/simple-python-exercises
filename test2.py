from common import show


@show
def max(a, b, c):
    a = a if a >= b else b
    return a if a >= c else c


assert max(1, 3, 4) == 4
assert max(3, 1, 2) == 3
assert max(2, 2, 1) == 2
assert max(5, 6, 7) == 7
assert max(-1, -2, -3) == -1
