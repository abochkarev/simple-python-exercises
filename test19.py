str_ = "%s bottles of beer on the wall, %s bottles of beer.\
 Take one down, pass it around, %s bottles of beer on the wall."


def sing_song(n=99):
    for i in xrange(n, 1, -1):
        print str_ % (i, i, i - 1)


sing_song()
