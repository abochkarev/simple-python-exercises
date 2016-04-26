def is_palindrome(str_):
    if str_ == '':
        return True
    if str_[0] == str_[-1]:
        return is_palindrome(str_[1:-1])
    else:
        return False


def palindrome_recognizer(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            print "Is '%s' palindrome? %s" % (line.strip(), is_palindrome(line.strip().lower()))


palindrome_recognizer('palindromes.txt')
