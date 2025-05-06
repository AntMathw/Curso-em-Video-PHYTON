#DESAFIO 058 DO CURSO EM VÍDEO PHYTON

import random

computador = random.randint(0, 10)
lista = [0, 10]
palpites = 0
print('Sou seu computador...\nAdvinha em um número que pensei de 0 a 10\nSerá que consegue advinhar? ')

acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Ta frio camarada...')
        if jogador > computador:
            print('Ta quente viu...')
print('Acertou com {} tentativas. PARABÉNS'.format(palpites))
