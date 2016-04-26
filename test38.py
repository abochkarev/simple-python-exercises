def calc_words_average(file_name):
    word_lens = 0
    word_counts = 0
    with open(file_name) as f:
        while True:
            data = f.readline().strip()
            if not data:
                break
            word_lens += len(data)
            word_counts += 1
    return word_lens / word_counts


print calc_words_average('semordnilaps.txt')
