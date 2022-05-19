import os
from pprint import pprint

BASE_PATH = os.getcwd()
FILES_DIR_NAME = 'Task open files2'

full_path = os.path.join(BASE_PATH, FILES_DIR_NAME)
file_list = os.listdir(path=full_path)


def file_merging():
    result = {}
    for filename in file_list:
        list_final = []
        with open(os.path.join(FILES_DIR_NAME, filename), 'r', encoding='utf-8') as file_obj:
            file_content = file_obj.read().split('\n')
            count_of_lines = len(file_content)
            list_final += [count_of_lines, file_content]
            d = {list_final[i]: list_final[i + 1] for i in range(0, len(list_final), 2)}
            sorted_tuple = sorted(d.items(), key=lambda x: x[0])
            result[filename] = sorted_tuple

        with open('out.txt', 'w', encoding='utf-8') as out:
            for key, val in result.items():
                out.write('{}:{}\n'.format(key, val))


file_merging()
