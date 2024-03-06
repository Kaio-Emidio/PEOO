# 2. Escreva um programa que verifica se um número fornecido pelo usuário é par
# ou ímpar.
        
n = int(input('Digite um número: '))
r = n % 2
if n == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')