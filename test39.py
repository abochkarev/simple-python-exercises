import random


def _play_game(start, stop):
    range_int = random.randrange(start, stop)
    print range_int
    name = raw_input("Hello! What is your name? ")
    print "Well, %s, I am thinking of a number between %s and %s." % (name, start, stop)
    count = 0
    while count < 3:
        guess = int(raw_input("Take a guess."))
        if guess < range_int:
            print "Your guess is too low."
        elif guess > range_int:
            print "Your guess is too high."
        else:
            print "Congratulation! That's it."
            break
        count += 1


def play_game():
    _play_game(1, 30)


play_game()
