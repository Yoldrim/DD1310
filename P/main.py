import re

from datetime import date

from PackingItem import PackingItem
from PackingList import PackingList

VALID_DATE_REGEX_PATTERN = r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$'
FILE_PATH = './db.txt'


def str_to_datetime_date(s):
    s_split = s.split('-')
    return date(int(s_split[0]), int(s_split[1]), int(s_split[2]))


def read_parse_file(file_path):
    file = open(file_path, 'r', encoding='utf8')
    segments = []
    lists = []

    while True:
        line1 = file.readline()
        line2 = file.readline()
        if not line2:
            break
        else:
            segments.append([line1, line2])
    file.close()

    for pair in segments:
        header_split, content_split = pair[0].split(';'), pair[1].split(';')
        l = PackingList(header_split[0], str_to_datetime_date(header_split[1].strip()))
        for item in content_split:
            item = item.strip('\n')
            l.items.append(PackingItem(item if item[0] != '+' else item[1:], item[0] == '+'))
        lists.append(l)

    return sorted(lists, key=lambda x: x.date)


def write_parse_file(file_path, lists):
    file = open(file_path, 'w', encoding='utf-8')
    for l in lists:
        file.write(f'{l.to_db_string()}\n')


def get_valid_input(prompt, condition, error_message):
    user_input = input(f"{prompt} ")

    try:
        if not condition(user_input):
            raise ValueError(error_message)
        return user_input
    except ValueError as e:
        print(e)
        return get_valid_input(prompt, condition, error_message)


def create_new_packing_list(pl_holder):
    print('Creating a new list')
    print('What should the list be named?')
    name = get_valid_input('>>>', lambda x: True, '')

    print('\nFor what date is the list going to be used? (Please use the date format YYYY-MM-DD)')
    d = get_valid_input('>>>', lambda x: re.match(VALID_DATE_REGEX_PATTERN, x),
                           "Please enter a valid date in this format: YYYY-MM-DD")
    print('\nList created!')
    pl_holder.append(PackingList(name, str_to_datetime_date(d)))


def search_lists_arr(pl_holder):
    print('Please enter your search phrase.')
    prompt = get_valid_input('>>>', lambda x: True, '')
    print('')
    matches = []
    for l in pl_holder:
        if l.name.find(prompt) >= 0:
            matches.append(l)

    if len(matches) == 1:
        selected_list_loop(matches[0])
    elif len(matches) > 1:
        print(f'Your search returned {len(matches)} results.')
        select_list_from_all(matches)
    else:
        print(f'No match found from your search {prompt}. Returning to main menu.')


def select_list_from_all(pl_holder):
    print('Select a packing list:')
    for i in range(0, len(pl_holder)):
        print(f'{i + 1}. {pl_holder[i].name} - {pl_holder[i].date}')
    c = get_valid_input('>>>', lambda x: x.isdigit() and int(x) in range(1, len(pl_holder) + 1),
                        'Please select a valid packing list number.')
    print('')
    selected_list_loop(pl_holder[int(c) - 1])


def selected_list_loop(selected_list):
    title = f'----- {selected_list.name} - {selected_list.date} -----'
    print(title)
    for item in selected_list.items:
        print(f'{"O" if item.packed else "X"} {item.name}')
    print('-' * len(title))
    print('1. Add item\n2. Mark item as packed\n3. Return to main menu')
    c = int(get_valid_input('>>>', lambda x: x.isdigit() and int(x) in range(1, 5), 'Please enter a valid option.'))
    print('')
    if c == 1:
        print('What item would you like to add?')
        new_item = get_valid_input('>>>', lambda x: True, '')
        print('')
        selected_list.items.append(PackingItem(new_item))
        return selected_list_loop(selected_list)
    elif c == 2:
        print('Which item would you like to mark as packed?')
        for i in range(0, len(selected_list.items)):
            print(f'{i + 1}. {selected_list.items[i].name}')
        item_to_mark = get_valid_input('>>>',
                                       lambda x: x.isdigit() and int(x) in range(1, len(selected_list.items) + 1),
                                       'Please enter a valid item number.')
        selected_list.items[int(item_to_mark) - 1].packed = True
        return selected_list_loop(selected_list)
    elif c == 3:
        return selected_list


packing_lists = read_parse_file(FILE_PATH)
while True:
    print(
        '\nWelcome to the packing list program!\nN New packing list\nA Show all lists\nU Show upcoming lists\nS Search for a list\nQ Quit')
    choice = get_valid_input('>>>', lambda x: x.upper() in ['N', 'A', 'U', 'S', 'Q'],
                             'Please enter a valid option.').upper()
    print('')
    if choice == 'N':
        create_new_packing_list(packing_lists)
    elif choice == 'A':
        select_list_from_all(packing_lists)
    elif choice == 'U':
        select_list_from_all(list(filter(lambda x: x.date >= date.today(), packing_lists)))
    elif choice == 'S':
        search_lists_arr(packing_lists)
    elif choice == 'Q':
        write_parse_file(FILE_PATH, packing_lists)
        print('Your packing lists are saved. See you again soon!')
        break
