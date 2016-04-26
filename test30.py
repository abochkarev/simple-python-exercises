from common import show

lexicon = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}


@show
def translate(list_):
    return map(lambda x: lexicon.get(x, None), list_)


assert translate(["merry", "christmas", "and", "happy", "new", "year"]) == ["god", "jul", "och", "gott", "nytt", "ar"]
