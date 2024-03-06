# 1. Crie um programa que pede ao usuário dois números e realiza as operações
# básicas de adição, subtração, multiplicação e divisão.

calc = True
while calc == True:
    print('Escolha o número referente a equação que deseja realizar:')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('0 - Sair')
    e = int(input())
    if e == 1:
        a = float(input('Digite um número: '))
        b = float(input('Digite outro número: '))
        print('O resultado é', a + b)
    if e == 2:
        a = float(input('Digite um número: '))
        b = float(input('Digite outro número: '))
        print('O resultado é', a - b)
    if e == 3:
        a = float(input('Digite um número: '))
        b = float(input('Digite outro número: '))
        print('O resultado é', a * b)
    if e == 4:
        a = float(input('Digite um número: '))
        b = float(input('Digite outro número: '))
        print('O resultado é', a / b)
    if e == 0:
        calc = False