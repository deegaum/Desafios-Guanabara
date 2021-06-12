from random import randint
digito = int(input('Escolha um número inteiro entre 0 e 5: '))
escolha = randint(1, 11)
if escolha == digito:
    print('Miseravi, vc acertou')
else:
    print(f'Tente outra vez meu consagrado, o número escolhido foi {escolha}')