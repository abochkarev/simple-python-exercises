from collections import defaultdict


class FileReader(object):
    def __init__(self, file_name):
        super(FileReader, self).__init__()
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name, mode='r') as f:
            return f.read().splitlines()


class AlternadesFinder(object):
    def __init__(self, words):
        super(AlternadesFinder, self).__init__()
        self.words = set(words)

    def find_alternades(self):
        alternades_map = defaultdict(list)
        for word in words:
            s1, s2 = word[0::2], word[1::2]
            if s1 in self.words and s2 in self.words:
                alternades_map[word].extend([s1, s2])
        return alternades_map


words = FileReader('unixdict.txt').read_file()
alternades = AlternadesFinder(words).find_alternades()
for k, v in alternades.items():
    print '"%s": makes "%s" and "%s".' % (k, v[0], v[1])
