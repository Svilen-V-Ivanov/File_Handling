from io import open

file_path = '.\\numbers.txt'

file = open(file_path, 'r')
sum = 0
for line in file:
    sum += int(line)

print(sum)
