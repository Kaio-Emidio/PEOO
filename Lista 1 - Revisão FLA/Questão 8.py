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