from common import show


@show
def filter_long_words(list_, n):
    return filter(lambda x: len(x) > n, list_)


assert filter_long_words(["favasdf", "sadf", "sa", "asfdef", "a"], 4) == ["favasdf", "asfdef"]
assert not filter_long_words(["favasdf", "sadf", "sa", "asfdef", "a"], 4) == ["favasdf", "asfdef", "sadfasdfeasef"]
