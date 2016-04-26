from common import show

alphabet = "abcdefghijklmnopqrstuvwxyz"


@show
def is_pangram(str_):
    c_alphabet = alphabet
    for w in str_:
        if w.isupper():
            w = w.lower()
        if w in c_alphabet:
            c_alphabet = c_alphabet.replace(w, "")
    return len(c_alphabet) == 0


assert is_pangram("The quick brown fox jumps over the lazy dog")
assert is_pangram("The quick brown fox jumps over the lazy dogg")
assert not is_pangram("AbcdefghijklmnopqrstuvwxY")
