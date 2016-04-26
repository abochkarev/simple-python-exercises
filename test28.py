from common import show


@show
def find_longest_word(list_):
    return reduce(max, map(len, list_))


assert not find_longest_word(["rqwe", "eradf", "fasdfew", "werfasdf", "afsdfaf", "sdsaf"]) == 4
assert find_longest_word(["rqwe", "eradf", "fasdfew", "werfasdf", "afsdfaf", "sdsafddddddddd"]) == 14
