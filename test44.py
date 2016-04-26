import random
from termcolor import colored


class Brackets(object):
    brackets = '[]'


class BracketsStringGenerator(object):
    start = 6
    stop = 16
    step = 2

    def generate_brackets_string(self):
        pse_int = random.randrange(self.start, self.stop, self.step)
        return ''.join(Brackets.brackets[random.getrandbits(1)] for _ in range(pse_int))


class BracketsStringValidator(object):
    @staticmethod
    def validate_brackets_string(brackets_string):
        string = brackets_string[:]
        while Brackets.brackets in string:
            string = string.replace(Brackets.brackets, '')

        if len(string) == 0:
            print colored('%s OK' % brackets_string, 'green')
        else:
            print colored('%s NOT OK' % brackets_string, 'red')

for _ in range(10):
    bsg = BracketsStringGenerator()
    bs = bsg.generate_brackets_string()

    bsv = BracketsStringValidator()
    bsv.validate_brackets_string(bs)
