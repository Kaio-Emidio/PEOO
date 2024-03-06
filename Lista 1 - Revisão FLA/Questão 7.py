# 7. Faça um programa que verifique se um número fornecido pelo usuário é
# primo ou não.

n = int(input('Digite um número: '))
if n % 2 != 0 and n % 3 != 0:
    print('O número é primo')
else: 
    print('O número é composto')