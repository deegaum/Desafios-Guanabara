slr = float(input('Digite o seu salário por favor: '))
if slr > 1250:
    print(f'O seu salário após o aumento será de R$ {slr+(slr*0.1)}')
else:
    print(f'O seu salário após o aumento será de R$ {slr+(slr*0.15)}')