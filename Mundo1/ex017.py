#DESAFIO 017 DO CURSO EM VÍDEO PHYTON

#Primeira Forma
from math import sqrt

cop = float(input('Digite o valor do cateto oposto: '))
cad = float(input('Digite o valor do cateto adjacente: '))
hip = cop**2 + cad**2
print('A hipotenusa vai medir {:.2f}'.format(sqrt(hip)))

#Segunda Forma 3 linha de código

import math
cop = float(input('Digite o valor do cateto oposto: '))
cad = float(input('Digite o valor do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(cop, cad)))
