from common import show


@show
def generate_n_chars(n, c):
    s = ""
    for i in xrange(n):
        s += c
    return s

assert generate_n_chars(2, "x") == "xx"
assert not generate_n_chars(2, "y") == "yyy"
