def char_freq_table(file_name):
    char_table = {}
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            for char in line:
                char_table[char] = char_table.get(char, 0) + 1
    for key, value in sorted(char_table.iteritems(), key=lambda (k, v): (v, k)):
        print "%s, %s" % (key, value)


char_freq_table("palindromes.txt")
