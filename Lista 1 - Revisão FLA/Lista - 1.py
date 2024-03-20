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

# 2. Escreva um programa que verifica se um número fornecido pelo usuário é par
# ou ímpar.
        
n = int(input('Digite um número: '))
r = n % 2
if n == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')

# 3. Crie um programa que converte a temperatura de Celsius para Fahrenheit e
# vice-versa, com base na escolha do usuário.
    
print('Digite o número referente ao processo que deseja fazer:')
print('1 - Celsius para Fahrenheit')
print('2 - Fahrenheit para Celcius')
o = int(input())
t = float(input('Digite a temperatura: '))
if o == 1:
    print('Essa temperatura em Fahrenheit é de: ', 5 / 9 * t + 32)
if o == 2:
    print('Essa temperatura em Celcius é de: ', 9 / 5 * t - 32)

# 4. Faça um programa que calcula a média de três notas fornecidas pelo usuário.

print('Digite três notas: ')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
print('A média dessas notas é de: ', (n1 + n2 + n3) / 3)

# 5. Escreva um programa que calcula o fatorial de um número fornecido pelo
# usuário.

n = int(input('Digite um número:'))
r = 1
for i in range(n):
    r *= (n - i)
print('O fatorial desse número é igual a: ', r)

# 6. Crie um programa que gera os primeiros N números da sequência de
# Fibonacci, onde N é fornecido pelo usuário.

n = int(input('Digite um número: '))
f = 0
b = 1
print(f)
print(b)
for _ in range(n-2):
    print(f + b)
    i = f + b
    f = b
    b = i

# 7. Faça um programa que verifique se um número fornecido pelo usuário é
# primo ou não.

n = int(input('Digite um número: '))
if n % 2 != 0 and n % 3 != 0:
    print('O número é primo')
else: 
    print('O número é composto')

# 8. Desenvolva um jogo em que o computador escolhe um número aleatório
# entre 1 e 100 e o usuário tenta adivinhar qual é esse número. O programa
# deve fornecer dicas dizendo se o número que o usuário escolheu é maior ou
# menor que o do computador.

import random

resposta = random.randrange(1, 100)
palpite = 0

while palpite != resposta:
    palpite = int(input('Chute um número: '))
    if palpite < resposta:
        print('A resposta é maior!')
    if palpite > resposta:
        print('A resposta é menor!')
    if palpite == resposta:
        print('Parabéns! Esse é o número correto!')

# 9. Escreva um programa que calcula o montante final de um investimento com
# base no capital inicial, taxa de juros e período de tempo fornecido pelo
# usuário.

C = float(input('Digite a capital inicial: '))
i = float(input('Digite a porcentagem de juros na forma decimal: '))
t = float(input('Digite o tempo: '))

print('O montante final é de: ', C * (1 + i) ** t)

# 10.Crie um programa que recebe os coeficientes (a,b,c) de uma equação
# quadrática ax e calcula suas raízes reais, se existirem.

#a=-1 b=20 c=--96

print('Primeiro digite o valor de "a", "b" e "c" na equação: ')
a = int(input('Valor de "a": '))
b = int(input('Valor de "b": '))
c = int(input('Valor de "c": '))


print('\n---------------------------------------------\n')


print('Para calcular delta utilizamos a seguinte fórmula:')
print('Δ = b^2 - 4 * a * c\n')
print('Substituindo os valores temos:')
print('Δ = {}^2 - 4 * {} * {}\n'.format(b, a, c))
print('Resolvendo as equações descobrimos o valor de delta.')
delta = (b ** 2) - 4 * a * c
print('Logo o valor de delta é: {}' .format(delta))


print('\n---------------------------------------------\n')


if delta < 0:
    print('Como delta é menor do que 0, então essa equação não possui raízes reais.')
else:
    print('Para encontrar as raízes utilizamos a seguinte fórmula:')
    print('x = -b ± √Δ\n')
    print('Essa fórmula deve ser calculada uma vez para +√Δ e uma segunda vez para –√Δ.\n')
    print('Então ficamos com:')
    print('x1 = (– b + √Δ) / (2 * a)')
    print('x2 = (– b - √Δ) / (2 * a)\n')
    print('Substituindo os valores temos:')
    print('x1 = (– {} + √{}) / (2 * {})' .format(b, delta, a))
    print('x2 = (– {} - √{}) / (2 * {})\n' .format(b, delta, a))
    print('Resolvendo as equações descobrimos o valor de x1 e x2.')


    x1 = (-b + delta ** (1/2)) / (2 * a)
    x2 = (-b - delta ** (1/2)) / (2 * a)


    print('Seu x1 é igual a: {}' .format(x1))
    print('Seu x2 é igual a: {}' .format(x2))