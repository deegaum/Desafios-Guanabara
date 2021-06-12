km = int(input('Eae irmão, quantos km tu vai passar nesse busão? '))
if (km <= 200):
    print(f'O valor da sua passagem será R$ {km*0.5}')
else:
    print(f'O valor da sua passagem será R$ {km*0.45}')