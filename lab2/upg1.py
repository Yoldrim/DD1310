driven_length = float(input('Ange körsträcka i km: '))
used_gas = float(input('Ange förbrukat bränsle i liter: '))
print(f'Bränsleförbrukningen för bilen är {round((100*used_gas) / driven_length, 3)} l/100 km.')
