from common import show

vowels = 'eyuioa'


@show
def is_vowel(char):
    return char in vowels


assert is_vowel('a')
assert not is_vowel('b')
