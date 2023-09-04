def calc_package_cost(w):
    cost = 0

    if w < 2:
        cost = w * 30
    elif w >= 2 and w < 6:
        cost = w * 28
    elif w >= 6 and w < 12:
        cost = w * 25
    elif w >= 12:
        cost = w * 23

    return cost


total_cost = 0
amount = int(input('Hur många paket vill du skicka? '))

i = 0
while i < amount:
    weight = float(input(f'Ange vikt för paket {i + 1}: '))
    total_cost += calc_package_cost(weight)
    i += 1

print(f'Det kommer att kosta {int(total_cost)} kr.')
