from io import open

#file_path = '.\\text.txt' #Found
file_path = '.\\text2.txt' #Not Found
try:
    open(file_path, 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')

