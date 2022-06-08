with open('.\\text.txt', 'r') as source_file:
    symbols_set = ["-", ",", ".", "!", "?"]
    for counter, line in enumerate(source_file):
        if counter % 2 == 0:
            edited_line = line.strip().split()
            edited_line = reversed(edited_line)
            edited_line = ' '.join(edited_line)
            for symbol in edited_line:
                if symbol in symbols_set:
                    edited_line = edited_line.replace(symbol, '@')

            print(edited_line)