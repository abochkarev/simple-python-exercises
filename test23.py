import re
from common import show


@show
def correct(str_):
    str_ = re.sub(r'\s+', ' ', str_)
    str_ = re.sub(r'[.]', '. ', str_)
    return str_


assert correct("This   is  very funny  and    cool.Indeed!") == "This is very funny and cool. Indeed!"
