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