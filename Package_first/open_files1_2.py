import os
from pprint import pprint

BASE_PATH = os.getcwd()
FILES_DIR_NAME = 'Task open files'
FILE_NAME = 'file.txt'

full_path = os.path.join(BASE_PATH, FILES_DIR_NAME, FILE_NAME)


def recipes():
    with open(full_path, encoding='utf-8') as file_obj:
        recipe_dict = {}
        dish = file_obj.readline().strip()
        for line in file_obj:
            quantity = int(line.strip())
            lines = []
            for item in range(quantity):
                data = file_obj.readline().strip().split(' | ')
                lines.append({'ingredient_name': data[0], 'quantity': data[1], 'measure': data[2]})
            recipe_dict[dish] = lines
            file_obj.readline()
            dish = file_obj.readline().strip()
    return recipe_dict


# pprint(recipes(), sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = recipes()
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for recipe in cook_book[dish]:
                if recipe['ingredient_name'] in shop_list:
                    shop_list[recipe['ingredient_name']]['quantity'] += int(recipe['quantity']) * person_count
                else:
                    shop_list[recipe['ingredient_name']] = {'measure': recipe['measure'],
                                                            'quantity': int(recipe['quantity']) * person_count}
                shop_list[recipe['ingredient_name']]['quantity'] += int(recipe['quantity']) * person_count
        return shop_list


# pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3), sort_dicts=False)
