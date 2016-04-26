import random


def read_word(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        line = lines[random.randrange(len(lines))]
        return line.strip()


def analize_word(hidden_word, suggested_word):
    analized_word = ''
    for i in range(len(suggested_word)):
        char = suggested_word[i]
        if char == hidden_word[i]:
            analized_word += '[' + char + ']'
        else:
            if suggested_word[i] in hidden_word:
                analized_word += '(' + char + ')'
            else:
                analized_word += char
    return analized_word

hidden_word = read_word('lingo.txt')
while True:
    suggested_word = raw_input()
    print 'Clue: %s' % analize_word(hidden_word, suggested_word)
    if suggested_word == hidden_word:
        break

