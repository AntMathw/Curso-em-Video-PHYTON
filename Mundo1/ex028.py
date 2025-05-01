#DESAFIO 028 DO CURSO EM VÍDEO

import random
from time import sleep

numero = random.randint(0, 5)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
escolha = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if numero == escolha:
    print('PARABÉNS! VOCÊ CONSEGUIU ME VENCER! ')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}'.format(numero, escolha))
