from os import remove
file_path = '.\\file_writer.txt'
try:
    remove(file_path)
except FileNotFoundError:
    print('File already deleted!')