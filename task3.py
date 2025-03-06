with open('1.txt', encoding='utf-8') as file_1:
    lines_1 = file_1.read().splitlines()
    f_1 = {
        'file_title': '1.txt',
        'length': str(len(lines_1)),
        'content': lines_1
    }

with open('2.txt', encoding='utf-8') as file_2:
    lines_2 = file_2.read().splitlines()
    f_2 = {
        'file_title': '2.txt',
        'length': str(len(lines_2)),
        'content': lines_2
    }

with open('3.txt', encoding='utf-8') as file_3:
    lines_3 = file_3.read().splitlines()
    f_3 = {
        'file_title': '3.txt',
        'length': str(len(lines_3)),
        'content': lines_3
    }

files_list = [f_1, f_2, f_3]
files_list.sort(key=lambda x: x['length'])

with open('task3.txt', 'a', encoding='utf-8') as file_4:
    for file in files_list:
        file_4.write(f"{file['file_title']}\n")
        file_4.write(f"{file['length']}\n")
        file_4.write(f"{'\n'.join(file['content'])}")
        file_4.flush()

