import re


def find_hapax(text):
    d = {}
    words = text.split()
    for word in words:
        word = re.sub(r'[^\w\s]', '', word)
        d[word] = d.get(word, 0) + 1
    for key, value in d.iteritems():
        if value == 1:
            print '%s %s' % (key, value)


text = 'A hapax legomenon (often abbreviated to hapax) is a word which occurs only ' \
       'once in either the written record of a language, the works of an author, or ' \
       'in a single text. Define a function that given the file name of a text will ' \
       'return all its hapaxes. Make sure your program ignores capitalization.'

find_hapax(text)
