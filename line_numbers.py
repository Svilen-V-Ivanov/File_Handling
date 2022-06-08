from string import punctuation

with open('.\\text.txt', 'r') as source_file, open('.\\output.txt', 'w') as output_file:
    symbols_set = set(punctuation)
    for counter, line in enumerate(source_file):
        line = line.strip()
        letters = 0
        symbols = 0
        for symbol in line:
            if symbol in symbols_set:
                symbols += 1
            elif symbol != ' ':
                letters += 1

        output_file.write(f"Line {counter + 1}: {line} ({letters})({symbols})\n")
