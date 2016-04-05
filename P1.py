from sys import argv
from re import findall
from collections import Counter

NUM_ARG = 3
NUM_WORDS = 5

if len(argv) != NUM_ARG:
    print("Pass two text files as arguments.")
else:
    file1 = open(argv[1], 'r')
    string1 = file1.read()
    file1.close()
    words1 = findall(r'\w+', string1)
    process_words1 = [word.lower() for word in words1]

    file2 = open(argv[2], 'r')
    string2 = file2.read()
    file2.close()
    words2 = findall(r'\w+', string2)
    process_words2 = [word.lower() for word in words2]

    common_words = set(process_words1).intersection(process_words2)
    all_words = process_words1 + process_words2
    all_common = [word for word in all_words if word in common_words]
    common_count = Counter(all_common)
    total_count = dict(Counter(all_words).most_common(NUM_WORDS))

    common_sorted = sorted(common_count, key=lambda word: (-common_count[word], word))
    total_sorted = sorted(total_count, key=lambda word: (-total_count[word], word))

    print('Words present in both files sorted by frequency:')
    print('Word        Frequency')
    print('---------------------')
    for word in common_sorted:
        print('{:<15}'.format(word), common_count[word])
    print()

    print('Top', NUM_WORDS, 'words present in either file: ')
    print('Word        Frequency')
    print('---------------------')
    for word in total_sorted:
        print('{:<15}'.format(word), total_count[word])









