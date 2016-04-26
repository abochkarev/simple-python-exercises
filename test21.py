from common import show


@show
def char_freq(str_):
    dict_ = {}
    for c in str_:
        dict_[c] = dict_.get(c, 0) + 1
    return dict_.values()

assert char_freq("aaabbbccc") == [3, 3, 3]
assert not char_freq("abbabcbdbabdbdbabababcbcbab") == [1, 2, 3, 4]
