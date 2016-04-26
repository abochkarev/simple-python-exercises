from common import show


@show
def filter_long_words(list_, n):
    return [x for x in list_ if n < len(x)]


assert filter_long_words(["abcd", "efgh", "ijklm", "nop"], 3) == ["abcd", "efgh", "ijklm"]
assert not filter_long_words(["abcd", "efgh", "ijklm", "nop"], 2) == ["abcd", "efgh", "ijklm"]
