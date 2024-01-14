import re

from datetime import date

from PackingItem import PackingItem
from PackingList import PackingList

# Regex pattern for valid date. 2024-01-14 = valid, 202-13-37 = not valid
VALID_DATE_REGEX_PATTERN = r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$'
ALLOWED_CHARACTERS_REGEX_PATTERN = r'^[a-zA-Z0-9_.-]*$'
FILE_PATH = './db.txt'


# Convert YYYY-MM-DD string to datetime object
def str_to_datetime_date(s):
    s_split = s.split('-')
    return date(int(s_split[0]), int(s_split[1]), int(s_split[2]))


# Read and parse packing lists file
def read_parse_file(file_path):
    file = open(file_path, 'r', encoding='utf8')
    segments = []
    lists = []

    while True:
        # Read file in pairs, break if there is no next pair
        line1 = file.readline()
        line2 = file.readline()
        if not line2:
            break
        else:
            segments.append([line1, line2])
    file.close()

    # Iterate over pairs
    for pair in segments:
        header_split, content_split = pair[0].split(';'), pair[1].split(';')
        # Create new packing list from pair
        l = PackingList(header_split[0], str_to_datetime_date(header_split[1].strip()))
        # Iterate over items in content line
        for item in content_split:
            # Clean up string
            item = item.strip('\n')
            # Create new packing item object from item, and append it to the newly created packing list
            l.items.append(PackingItem(item if item[0] != '+' else item[1:], item[0] == '+'))
        lists.append(l)

    # Return all lists, sorted by date
    return sorted(lists, key=lambda x: x.date)


# Parse and write packing lists to file
def write_parse_file(file_path, lists):
    file = open(file_path, 'w', encoding='utf-8')
    for l in lists:
        file.write(f'{l.to_db_string()}\n')


# Recursive loop for getting input
def get_valid_input(prompt, condition, error_message):
    # Get user input
    user_input = input(f"{prompt} ")

    try:
        # Throw error if set condition is not valid on user input
        if not condition(user_input):
            raise ValueError(error_message)
        # Return input
        return user_input
    except ValueError as e:
        # Print error
        print(e)
        # Call itself to try again
        return get_valid_input(prompt, condition, error_message)


# Function for creating new packing lists from user input
def create_new_packing_list(pl_holder):
    print('Creating a new list')
    print('What should the list be named?')
    name = get_valid_input('>>>', lambda x: re.match(ALLOWED_CHARACTERS_REGEX_PATTERN, x), 'The list name must only contain alphanumeric characters')

    print('\nFor what date is the list going to be used? (Please use the date format YYYY-MM-DD)')
    d = get_valid_input('>>>', lambda x: re.match(VALID_DATE_REGEX_PATTERN, x),
                        "Please enter a valid date in this format: YYYY-MM-DD")
    print('\nList created!')
    # Create new PackingList and append it to packing list holder by reference
    pl_holder.append(PackingList(name, str_to_datetime_date(d)))


# Function for searching packing list holder
def search_lists_arr(pl_holder):
    print('Please enter your search phrase.')
    # Get search phrase
    prompt = get_valid_input('>>>', lambda x: True, '')
    print('')
    matches = []
    # Iterate over lists in packing list holder, if match, add to matches
    for l in pl_holder:
        if l.name.find(prompt) >= 0:
            matches.append(l)

    # If only one match, move into selected_list_loop, allowing user to interact with selected list
    if len(matches) == 1:
        selected_list_loop(matches[0])
    # If multiple matches, send user to select list from matches
    elif len(matches) > 1:
        print(f'Your search returned {len(matches)} results.')
        select_list_from_all(matches)
    else:
        print(f'No match found from your search {prompt}. Returning to main menu.')


# Function for selecting a list from supplied lists
def select_list_from_all(pl_holder):
    print('Select a packing list:')
    # Print lists with corresponding number to ease selection
    for i in range(0, len(pl_holder)):
        print(f'{i + 1}. {pl_holder[i].name} - {pl_holder[i].date}')
    # Get choice. Make sure it is valid number from print above.
    c = get_valid_input('>>>', lambda x: x.isdigit() and int(x) in range(1, len(pl_holder) + 1),
                        'Please select a valid packing list number.')
    print('')
    # Move into selected_list_loop, allowing user to interact with selected list
    selected_list_loop(pl_holder[int(c) - 1])


# Recursive function for interacting with a selected list
def selected_list_loop(selected_list):
    # Print info about list, and available actions
    title = f'----- {selected_list.name} - {selected_list.date} -----'
    print(title)
    for item in selected_list.items:
        print(f'{"O" if item.packed else "X"} {item.name}')
    print('-' * len(title))
    print('1. Add item\n2. Mark item as packed\n3. Return to main menu')

    # Get user action
    c = int(get_valid_input('>>>', lambda x: x.isdigit() and int(x) in range(1, 3), 'Please enter a valid option.'))
    print('')
    if c == 1:
        print('What item would you like to add?')
        # Get item
        new_item = get_valid_input('>>>', lambda x: True, '')
        print('')
        # Append item to packing list
        selected_list.items.append(PackingItem(new_item))
        # Go again
        return selected_list_loop(selected_list)
    elif c == 2:
        print('Which item would you like to mark as packed?')
        # Print available items
        for i in range(0, len(selected_list.items)):
            print(f'{i + 1}. {selected_list.items[i].name}')
        # Get choice. Make sure it is valid number from print above
        item_to_mark = get_valid_input('>>>',
                                       lambda x: x.isdigit() and int(x) in range(1, len(selected_list.items) + 1),
                                       'Please enter a valid item number.')
        # Set selected item as packed
        selected_list.items[int(item_to_mark) - 1].packed = True
        # Go again
        return selected_list_loop(selected_list)
    elif c == 3:
        # Break loop and return list
        return selected_list


# Read list from txt
packing_lists = read_parse_file(FILE_PATH)
# Main loop
while True:
    # Print menu message
    print(
        '\nWelcome to the packing list program!\nN New packing list\nA Show all lists\nU Show upcoming lists\nS Search for a list\nQ Quit')
    # Get valid user choice
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
