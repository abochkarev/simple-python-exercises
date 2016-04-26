import re


class FileReader(object):
    def __init__(self, file_name):
        super(FileReader, self).__init__()
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name) as f:
            return f.read()


class SentenceSplitter(object):

    def __init__(self, sentence):
        super(SentenceSplitter, self).__init__()
        self.sentence = sentence

    def split_sentence(self):
        sentence = self.sentence.replace('\n', '')
        sentence = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentence)
        sentence = re.sub(r'\? ', '?\n', sentence)
        return sentence.split('\n')


class SentencePrinter(object):
    def __init__(self, sentences):
        super(SentencePrinter, self).__init__()
        self.sentences = sentences

    def print_sentences(self):
        for sentence in self.sentences:
            print sentence


file_reader = FileReader('text.txt')
sentence_ = file_reader.read_file()

sentence_splitter = SentenceSplitter(sentence_)
sentences_ = sentence_splitter.split_sentence()

sentence_printer = SentencePrinter(sentences_)
sentence_printer.print_sentences()
