from common import show

consonant = "qwrtpsdfghjklzxcvbnm"
vowel = "eyuioa"

@show
def make_ing_form(str_):
    if str_.endswith("ie"):
        return str_[:-2] + "ying"
    elif str_.endswith("e") and str_ not in ("be", "see", "knee"):
        return str_[:-1] + "ing"
    elif str_[-1] in consonant and str_[-2] in vowel and str_[-3] in consonant:
        return str_ + str_[-1] + "ing"
    else:
        return str_ + "ing"

assert make_ing_form("lie") == "lying"
assert make_ing_form("see") == "seeing"
assert make_ing_form("move") == "moving"
assert make_ing_form("hug") == "hugging"
