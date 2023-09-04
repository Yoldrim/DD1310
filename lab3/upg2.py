def get_input_in_interval(prompt, max, min):
    inp = int(input(prompt))
    if inp >= min and inp <= max:
        return inp
    else:
        print(f'Ange ett nummer mellan {min} och {max}.')
        return get_input_in_interval(prompt, max, min)


rows = get_input_in_interval('Ange antal rader: ', 9, 1)
columns = get_input_in_interval('Ange antal kolumner: ', 9, 1)

i, j = 0, 1

while i <= rows:
    print(f'{i if i > 0 else " ":<3}', end='')
    while j <= columns:
        print(f'{(i if i > 0 else 1)*j:<3}', end='')
        j += 1
    j = 1
    i += 1
    print('')
