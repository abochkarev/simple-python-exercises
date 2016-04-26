from common import show


@show
def reverse(s):
    if len(s) == 0:
        return ""
    return s[len(s) - 1] + reverse(s[:len(s) - 1])


assert reverse("I am testing") == "gnitset ma I"
assert not reverse("am") == "am"
assert reverse("ma") == "am"
