def create_chocolate_bar(x, y):
    if x <= 0 or y <= 0:
        return None
    tmp = [[str(i+1) + str(j+1) for j in range(y)] for i in range(x)]
    tmp[0][0] = 'P'
    return tmp


def print_chocolate_bar(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(f'{arr[i][j]:<3}', end='')
        if len(arr[i]) > 0:
            print('')


def chomp(arr, x, y):
    for i in range(x, len(arr)):
        arr[i] = arr[i][0:y]


def check_winner(arr):
    return [item for sub in arr for item in sub] == ['P']


def ask_cell_number(arr):
    val = input('Välj en ruta: ')
    try:
        if arr[int(val[0]) - 1][int(val[1]) - 1] is not None:
            return int(val[0]) - 1, int(val[1]) - 1
    except IndexError:
        print(f'Fel val, ruta {val} finns inte i spelplanen, försök igen!')
        return ask_cell_number(arr)


print('Välkommen till spelet Chomp. \n\nInstruktioner: I spelet kommer du utmanas om att välja ett blocknummer '
          'från spelplanen. Det valda blocket och alla block under och till högre kommer att raderas. Spelet går ut '
          'på att undvika välja P, den spelare som väljer P förlorar och den andra spelare vinner.')

is_player_one = False
rows = int(input('Hur många rader ska chokladbaren bestå av: '))
columns = int(input('Hur många kolumner ska chokladbaren bestå av: '))
bar = create_chocolate_bar(rows, columns)
print_chocolate_bar(bar)

while check_winner(bar) is not True:
    is_player_one = not is_player_one
    print(f'Spelare {"#1" if is_player_one else "#2"}.')
    r, c = ask_cell_number(bar)
    chomp(bar, r, c)
    print('')
    print_chocolate_bar(bar)
    print('')
    # print(bar)

print(f'Spelet är slut, vinnare är spelare {"#1" if is_player_one else "#2"}!')
