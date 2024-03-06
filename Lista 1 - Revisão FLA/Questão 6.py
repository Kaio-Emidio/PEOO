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