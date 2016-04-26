import os

d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
     'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
     'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo',
     's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
     'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}


# espeak must be installed: sudo apt-get install espeak
def spoken_icao(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            for char in line:
                os.system('espeak ' + d.get(char))


spoken_icao('semordnilaps.txt')