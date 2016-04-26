def are_semordnilaps(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in xrange(len(str1)):
        if str1[i] != str2[-1-i]:
            return False
    return True


def semordnilaps_recognizer(file_name):

    with open(file_name) as f:
        lines = f.readlines()
        for str1 in lines:
            for str2 in lines:
                str1 = str1.strip().lower()
                str2 = str2.strip().lower()
                if str1 != str2 and are_semordnilaps(str1, str2):
                    print "Semordnilaps are: %s %s" % (str1, str2)


semordnilaps_recognizer('semordnilaps.txt')
