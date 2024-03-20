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