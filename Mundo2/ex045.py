#DESAIO 045 DO CURSO EM VÍDEO PHYTON
from time import sleep
import random


jogador = int(input('SUAS OPÇÕES:\n[ 1 ]PEDRA\n[ 2 ]TESOURA\n[ 3 ]PAPEL\nQual sua jogada? '))
computador = random.randint(1, 3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-' * 20)
print('O jogador escolheu {}'.format(jogador))
print('O computador escolheu {}'.format(computador))

if computador == 1:
    if jogador == 2:
        print('Computador ganhou')
if jogador == 1:
    if computador == 3:
        print('Computador GANHOU')
if jogador == 2:
    if computador == 1:
        print('Computador GANHOU')
if jogador == 3:
    if computador == 2:
        print('Computador GANHOU')
if jogador == 1:
    if computador == 2:
        print('Jogador GANHOU')
if jogador == 3:
    if computador == 1:
        print('Jogador GANHOU')
if jogador == 2:
    if computador == 3:
        print('Jogador GANHOU')
else:

    if jogador == 2:
        if computador == 2:
            print('EMPATE')
    if jogador == 3:
        if computador == 3:
            print('EMPATE')

