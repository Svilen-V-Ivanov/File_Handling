import re


def read_words():
    with open('.\\words.txt', 'r') as file:
        return file.read().split(' ')


def count_words_in_file(words):
    word_counts = {
        word: 0 for word in words
    }
    with open('.\\input.txt', 'r') as file:
        for line in file:
            words_in_line = [w.lower() for w in re.findall(r'\b\S+\b', line)]
            for word in words:
                word_counts[word] += words_in_line.count(word.lower())
    return word_counts


words_counts = count_words_in_file(read_words())
words_counts_sorted = sorted(words_counts.items(), key=lambda x: x[1], reverse=True)

file = open('.\\output.txt', 'w')
for w, c in words_counts_sorted:
    file.write(f'{w} - {c}')
    file.write('\n')
file.close()
