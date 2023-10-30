### UPG 1 ###

driven_length = float(input('Ange körsträcka i km: '))
used_gas = float(input('Ange förbrukat bränsle i liter: '))
print(f'Bränsleförbrukningen för bilen är {round((100*used_gas) / driven_length, 3)} l/100 km.')

#############

### UPG 2 ###

weight = float(input('Hur mycket väger paketet: '))
cost = 0

if weight < 2:
    cost = weight * 30
elif weight >= 2 and weight < 6:
    cost = weight * 28
elif weight >= 6 and weight < 12:
    cost = weight * 25
elif weight >= 12:
    cost = weight * 23

print(f'Det kommer att kosta {round(cost, 2)} kr.')

#############

### UPG 3 ###

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

#############