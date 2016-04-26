from collections import defaultdict


class FileReader(object):

    def __init__(self, file_name):
        super(FileReader, self).__init__()
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name, mode='r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                yield line.rstrip()


class WordFinder(object):

    def __init__(self, text):
        super(WordFinder, self).__init__()
        self.words_map = defaultdict(list)
        for line in text:
            sorted_line = ''.join(sorted(line))
            self.words_map[sorted_line].append(line)

    def find_words(self):
        return filter(lambda x: len(x) > 1, self.words_map.values())


class WordPrinter(object):

    def __init__(self, words):
        super(WordPrinter, self).__init__()
        self.words = words

    def print_words(self):
        for word in self.words:
            print word

file_reader = FileReader('unixdict.txt')
text_ = file_reader.read_file()

word_finder = WordFinder(text_)
words_ = word_finder.find_words()

word_printer = WordPrinter(words_)
word_printer.print_words()
