import os

def make_files_dict(folder_path):
    all_items = os.listdir(folder_path)
    all_files_list = []
    for file_name in all_items:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, encoding='utf-8') as f:
            f.seek(0)
            lines = f.read().splitlines()
            file_dict = {
                'file_title': file_name,
                'length': str(len(lines)),
                'content': lines
            }
        all_files_list.append(file_dict)
    return all_files_list

def create_common_file(folder_path, new_file_name):
    all_files_list = make_files_dict(folder_path)
    all_files_list.sort(key=lambda x: x['length'])
    
    with open(new_file_name, 'a', encoding='utf-8') as f:
        for file in all_files_list:
            f.write(f"{file['file_title']}\n")
            f.write(f"{file['length']}\n")
            f.write(f"{'\n'.join(file['content'])}\n")
            f.flush()
    print(f'Файл {new_file_name} готов!')

folder_path = "to_proccess"
new_file_name = 'task3.txt'
create_common_file(folder_path, new_file_name)