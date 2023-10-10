from TV import TV


def magic_number_input(prompt, min, max):
    try:
        choice = int(input(prompt))
    except ValueError:
        print('Du måste skriva in ett giltigt nummer!')
        return magic_number_input(prompt, min, max)

    if choice >= min and choice <= max:
        return choice
    else:
        print('Jag förstår inte vad du menar, försök igen.')
        return magic_number_input(prompt, min, max)


def read_file(file):
    tvs = []
    f = open(file, 'r', encoding='utf8')
    for line in f:
        line = line.replace('\n', '')
        line = line.split(',')
        tvs.append(TV(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4])))
    return tvs


def write_file(tv_list, file):
    out_str = ''
    for tv in tv_list:
        out_str += f"{tv.str_for_file()}\n"
    f = open(file, 'w', encoding='utf8')
    f.write(out_str)


def change_channel(tv):
    choice = magic_number_input('Kanal: ', -99999, 99999)
    while not tv.change_channel(choice):
        choice = magic_number_input(f"Kanal för den här TV:n ska vara mellan 1 till #{tv.max_channels}, försök igen:", -99999, 99999)


def increase_volume(tv):
    tv.increase_volume()


def decrease_volume(tv):
    tv.decrease_volume()


def adjust_TV_menu():
    print('1. Byt kanal')
    print('2. Sänk ljudnivå')
    print('3. Höj ljudnivå')
    print('4. Gå tillbaka till huvudmenyn')
    return magic_number_input('Välj: ', 1, 4)


def select_TV_menu(tv_list):
    for i in range(len(tv_list)):
        print(f"{i + 1}. {tv_list[i].tv_name}")
    print(f"{len(tv_list) + 1}. Avsluta")

    return tv_list[magic_number_input('Välj: ', 1, len(tv_list) + 1)]


tv_obj_list = read_file('db.txt')
selected_tv = None