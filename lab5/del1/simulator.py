from TV import TV

FILE_NAME = 'db.txt'

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


def number_input(prompt, min, max):
    try:
        inp = int(input(prompt))
    except ValueError:
        print('Du måste skriva in ett tal, försök igen.')
        return number_input(prompt, min, max)

    if inp >= min and inp <= max:
        return inp
    else:
        print(f'Du måste skriva in ett nummer i spannet {min}-{max}, försök igen!')
        return number_input(prompt, min, max)


def change_channel(tv_instance):
    inp = number_input('Välj kanal: ', 0, tv_instance.max_channels)
    if not tv_instance.change_channel(inp):
        print(f'Kunde inte ändra kanal till {inp}. Försök igen.')


def increase_volume(tv_instance):
    if not tv_instance.increase_volume():
        print('Volymen är på max!')


def decrease_volume(tv_instance):
    if not tv_instance.decrease_vollume():
        print('Volymen är på 0.')


def adjust_TV_menu(tv_instance):
    print(f'\n{tv_instance.tv_name}')
    print(f'Kanal: {tv_instance.current_channel}')
    print(f'Volym: {tv_instance.current_volume}')

    print('\n1. Byt kanal')
    print('2. Höj volymen')
    print('3. Sänk volymen')
    print('4. Gå tillbaks till huvudmenyn')

    return number_input('Välj: ', 1, 4)

def select_TV_menu(tvs):
    while True:
        for i in range(len(tvs)):
            print(f'{i+1}. {tvs[i].tv_name}')
        print(f'{len(tvs)+1}. Avsluta')
        inp = number_input('Välj: ', 1, len(tvs)+1)
        if inp == len(tvs)+1:
            write_file(tvs, FILE_NAME)
            print('Simulering avslutad.')
            break
        else:
            active_tv = tvs[inp-1]
            while True:
                choice = adjust_TV_menu(active_tv)
                if choice == 1:
                    change_channel(active_tv)
                elif choice == 2:
                    increase_volume(active_tv)
                elif choice == 3:
                    decrease_volume(active_tv)
                else:
                    break


tvlista = read_file(FILE_NAME)
select_TV_menu(tvlista)
