### UPG 1 ###

def c_to_f(c):
    return round((c*9+160) / 5, 1)


print(f"{'C':<4}{'F':<4}")
for i in range(20):
    print(f'{i:<4}{c_to_f(i):<4}')


#############

### UPG 2 ###

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

#############

### UPG 3 ###

import random


def throw_dies(count):
    return [random.randint(1, 6) for _ in range(count)]


dies = int(input('Hur många tärningar behövs i spelet? '))
max_throws = int(input('Hur många kast får en spelare? '))
throws = 0

while True:
    io = input('Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A: ')
    throws = 0
    if io.lower() == 'a':
        break

    while True:
        result = throw_dies(dies)
        throws += 1
        for i in range(len(result)):
            print(f'Tärning {i+1}: {result[i]}')

        print(' ')
        if throws < max_throws:
            io2 = input('Är du inte nöjd kan du kasta igen. Vill du kasta igen? (J/N) ')
            if io2.lower() == 'n':
                print(f'Du fick {str(result)[1:-1]}.')
                break
        else:
            print(f'Du fick {str(result)[1:-1]}.')
            break

print('\nTack och hej!')


#############