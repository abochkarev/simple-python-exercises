from common import show


@show
def find_longest_word(list_):
    if not list_:
        raise RuntimeError("List shouldn't be none or empty")
    max_length = len(list_[0])
    for i in xrange(1, len(list_)):
        if len(list_[i]) > max_length:
            max_length = len(list_[i])
    return max_length


assert find_longest_word(["abc", "cdf", "fgh", "a"]) == 3
assert find_longest_word(["a", "bb"]) == 2
assert not find_longest_word(["a", "bbb"]) == 2

