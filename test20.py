from common import show

bilingual_lex = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}

@show
def translate(str_):
    return " ".join([bilingual_lex.get(x) for x in str_.split()])


assert translate("merry christmas and happy new year") == "god jul och gott nytt ar"
assert not translate("merry christmas and happy new year") == "god jul och gott nytt"

