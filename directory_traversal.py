#Програмата търси само в първото ниво на директорията, както е по условие.
from os import listdir

directory = str(input())
output_directory = str(input())
result = {}

for element in listdir(directory):
    extension = element.split('.')[-1]
    if extension not in result:
        result[extension] = []
    result[extension].append(element)

with open(f'{output_directory}\\report.txt', 'w') as output_file:
    for key, value in sorted(result.items(), key=lambda x: (x[0], x[1])):
        output_file.write(f".{key}" + '\n')
        for file in value:
            output_file.write(f"- - - {file}\n")
