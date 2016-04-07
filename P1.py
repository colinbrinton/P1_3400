# AUTHOR: Colin Brinton
# FILENAME: P1.py
# DATE: 04/05/2016
# REVISION HISTORY: 1.0

from sys import argv
from collections import Counter
from string import punctuation

NUM_ARG = 3
NUM_WORDS = 5
FILE_ONE = 1
FILE_TWO = 2


def get_words(arg_num):
    file = open(argv[arg_num], 'r')
    raw_text = file.read()
    file.close()

    words = [word.strip(punctuation) for word in raw_text.split() if word.strip(punctuation) != '']
    process_words = [word.lower() for word in words if word.isalpha()]
    return process_words

try:
    words1 = get_words(FILE_ONE)
    words2 = get_words(FILE_TWO)

    common_words = set(words1).intersection(words2)
    all_words = words1 + words2
    all_common = [word for word in all_words if word in common_words]
    common_count = Counter(all_common)
    total_count = dict(Counter(all_words).most_common(NUM_WORDS))

    common_sorted = sorted(common_count, key=lambda word: (-common_count[word], word))
    total_sorted = sorted(total_count, key=lambda word: (-total_count[word], word))

    print('Words present in both files sorted by frequency:')
    print('Word        Frequency')
    print('---------------------')
    for word in common_sorted:
        print('{:15}'.format(word), common_count[word])
    print()

    print('Top', NUM_WORDS, 'words present in either file: ')
    print('Word        Frequency')
    print('---------------------')
    for word in total_sorted:
        print('{:15}'.format(word), total_count[word])

except IndexError:
    print('Pass two text files as command line arguments:')
    print('P1.py <file1>.txt <file2>.txt')