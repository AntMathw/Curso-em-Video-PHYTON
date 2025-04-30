#DESAFIO 018 DO CURSO EM VÍDEO PHYTON

#Primeira Forma
from math import  radians, sin, cos, tan

angulo = int(input('Digite o angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {} seu SENO é {:.2f}'.format(angulo, seno))
print('O angulo de {} seu COSSENO é {:.2f}'.format(angulo, cosseno))
print('O anmulo de {} sua TANGENTE é {:.2f}'.format(angulo, tangente))

#Segunda Forma com 5 linha de Códio
import math

angulo = int(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O angulo de {} seu SENO É {:.2f} \nO angulo de {} seu COSSENO é {:.2f}\nO angulo {} sua TANGENTE é {:.2f}'.format(angulo, seno, angulo, cos, angulo, tan))
