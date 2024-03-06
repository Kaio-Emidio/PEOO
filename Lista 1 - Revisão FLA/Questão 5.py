# 5. Escreva um programa que calcula o fatorial de um número fornecido pelo
# usuário.

n = int(input('Digite um número:'))
r = 1
for i in range(n):
    r *= (n - i)
print('O fatorial desse número é igual a: ', r)