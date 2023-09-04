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
