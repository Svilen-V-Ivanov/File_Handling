from os import remove
from os.path import exists

while True:
    command = input()

    if command == 'End':
        break

    command_parts = command.split('-')
    order, file_name = command_parts[0], command_parts[1]

    if order == 'Create':
        with open(f'.\\{file_name}', 'w') as new_file:
            pass
    elif order == 'Add':
        content = command_parts[2]
        with open(f'.\\{file_name}', 'a') as current_file:
            current_file.write(content + '\n')
    elif order == 'Replace':
        if not exists(f'.\\{file_name}'):
            print("An error occurred.")
            continue

        old_string, new_string = command_parts[2], command_parts[3]
        with open(f'.\\{file_name}', 'r+') as current_file:
            all_text = current_file.read().replace(old_string, new_string)
            current_file.seek(0)
            current_file.truncate()
            current_file.write(all_text)
    else:
        if not exists(f'.\\{file_name}'):
            print("An error occurred.")
            continue
        remove(f'.\\{file_name}')
