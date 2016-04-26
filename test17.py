import regex as re
from common import show


@show
def is_palindrome(str_, prepared=False):
    if not prepared:
        str_ = re.sub(r'[^a-z0-9]', "", str_.lower())
        prepared = True
    if str_ == "":
        return True
    elif str_[0] == str_[len(str_)-1]:
        return is_palindrome(str_[1:len(str_)-1], prepared)
    else:
        return False

assert is_palindrome("Go hang a salami I'm a lasagna hog.")
assert is_palindrome("Was it a rat I saw?")
assert is_palindrome("Step on no pets")
assert is_palindrome("Sit on a potato pan, Otis")
assert is_palindrome("Lisa Bonet ate no basil")
assert is_palindrome("Satan, oscillate my metallic sonatas")
assert is_palindrome("I roamed under it as a tired nude Maori")
assert is_palindrome("Rise to vote sir")
assert is_palindrome("Dammit, I'm mad!")







