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
