#DESAFIO 006 DO CURSO EM VÍDEO PHYTON

#Primeira Forma utilizando a importação MATH, disponibilizando varias formulas. Mas eu utilizei o SQRT(Raiz quadrada)
import math

numero = int(input('Digite um valor: '))
print('Analisando o valor {} \nseu dobro é {} \nseu triplo é {} \nsua raiz quadrada é {:.1f}'.format(numero, numero * 2, numero * 3, math.sqrt(numero)))

#Segunda Forma
numero = int(input('Digite um valor: '))
print('Analisando o valor {} \nseu dobro é {} \nseu triplo é {} \n sua raiz quadrada é {:.1f}'.format(numero, numero * 2, numero * 3, numero ** (1/2)))
