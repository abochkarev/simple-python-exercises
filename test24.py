from common import show


@show
def make_3sg_form(str_):
    for suffix in ["o", "ch", "s", "sh", "x", "z"]:
        if str_.endswith(suffix):
            return str_ + "es"
    if str_.endswith("y"):
        return str_[:-1] + "ies"
    return str_ + "s"


assert make_3sg_form("try") == "tries"
assert make_3sg_form("brush") == "brushes"
assert make_3sg_form("run") == "runs"
assert make_3sg_form("fix") == "fixes"
