# 9. Escreva um programa que calcula o montante final de um investimento com
# base no capital inicial, taxa de juros e período de tempo fornecido pelo
# usuário.

C = float(input('Digite a capital inicial: '))
i = float(input('Digite a porcentagem de juros na forma decimal: '))
t = float(input('Digite o tempo: '))

print('O montante final é de: ', C * (1 + i) ** t)