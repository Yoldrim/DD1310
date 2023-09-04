def c_to_f(c):
    return round((c*9+160) / 5, 1)


print(f"{'C':<4}{'F':<4}")
for i in range(20):
    print(f'{i:<4}{c_to_f(i):<4}')
