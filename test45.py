import re


class FileReader(object):
    def __init__(self, file_name):
        super(FileReader, self).__init__()
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name, mode='r') as f:
            return re.findall('\w+', f.read())


class MaxChainFinder(object):
    def __init__(self, words):
        super(MaxChainFinder, self).__init__()
        self.words_map = dict([(word, []) for word in words])
        [self.words_map[w1].append(w2) for w1 in words
         for w2 in words if w1[-1] == w2[0] and w1 != w2]

    def _find_max_chain(self, chain):
        words = self.words_map.get(chain[-1])
        if not words:
            return chain
        max_chains = (self._find_max_chain(chain + [w])
                      if w not in chain else chain for w in words)
        return max(max_chains, key=len)

    def find_max_chain(self):
        max_chains = (self._find_max_chain([w]) for w in self.words_map)
        return max(max_chains, key=len)


file_reader = FileReader('pokemons.txt')
text_ = file_reader.read_file()

chain_finder = MaxChainFinder(text_)
max_chain = chain_finder.find_max_chain()
print 'Length = %s, chain = %s' % (len(max_chain), max_chain)
