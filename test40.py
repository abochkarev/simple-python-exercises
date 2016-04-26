import random


def read_colors(file_name):
    colors = []
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip()
            colors.append(line)
    return colors


def choose_color(colors):
    return colors[random.randrange(1, len(colors))]


def mixup_chars(color):
    color = list(color)
    random.shuffle(color)
    return ''.join(color)


colors = read_colors('colors.txt')
color = choose_color(colors)
anagram = mixup_chars(color)
color_anagram = {color: anagram}
print 'Colour word anagram: %s' % anagram
while True:
    input = raw_input('Guess the colour word!')
    if color_anagram.get(input, None) == anagram:
        print 'Correct!'
        break
