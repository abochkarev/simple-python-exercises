from common import show


@show
def is_palindrome(str):
    if len(str) == 0:
        return True

    if str[0] == str[len(str) - 1]:
        return is_palindrome(str[1:len(str) - 1])
    else:
        return False


assert is_palindrome("radar")
assert not is_palindrome("racdar")
assert is_palindrome("arozaupalanalapuazora")
