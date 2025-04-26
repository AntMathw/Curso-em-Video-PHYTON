#AVISO CARO DOCENTE DO CURSO EM VÍDEO, ESSA SÃO APENAS RESOLUÇÕES COM BASE EM MINHA VISAO, TENTA NÃO COPIAR E FAZER O SEU PRÓPRIO
#LEMBRANDO QUE É MUITO IMPORTANTE À PRATICA NO SEU APRENDIZADO, ANTES DE VER CÓDIGO PRONTO
#ESSE REPOSITÓRIO E PARA FINS EDUCATIVOS, PARA CORREÇÕES OU NÃO SOUBER COMO FAZER SUA PRÓPRIA RESOLUÇÃO
#SITE DO CURSO DE PHYTON www.cursoemvideo.com
#CURSO APRESENTADO POR GUSTAVO GUANABARA
#STAY FOCUSED STUDENT, PRACTICE AND STUDY WILL HELP YOUR LEARNING.


#DESAFIO 001 DO CURSO EM VÍDEO PHYTON

  #Primero Formato
print('Olá, Mundo!')

  #Segundo Formato
mensagem = 'Olá, Mundo!'
print(mensagem)

#DESAFIO 002 DO CURSO EM VÍDEO PHYTON

nome = str(input('Digite seu nome: '))
print('é um Prazer em conhecer-lo {}'.format(nome))

#DESAFIO 003 DO CURSO EM VÍDEO PHYTON

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor:: '))
print('A soma entre {} e {} é igual a {}'.format(num1, num2, num1+num2))

#DESAFIO 005 DO CURSO EM VÍDEO PHYTON

nome = input('Digite algo: ')
print('O tipo primitivo é: ', type(nome))
print('So tem espaços? {}'.format(nome.isspace()))
print('é um número? {}'.format(nome.isnumeric()))
print('É analfabético? {}'.format(nome.isalpha()))
print('É alfanumérico? {}'.format(nome.isalnum()))
print('Está em MAIUSCULO? {}'.format(nome.isupper()))
print('Está em minusculo? {}'.format(nome.islower()))
print('Está capitalizada? {}'.format(nome.istitle()))

#DESAFIO 005 DO CURSO EM VÍDEO PHYTON

numero = int(input('Digite um valor: '))
print('Analisando o valor {}, seu antecessor é {}, e seu sucessor {}'.format(numero, numero - 1, numero + 1))

#DESAFIO 006 DO CURSO EM VÍDEO PHYTON

#Primeira Forma utilizando a importação MATH, disponibilizando varias formulas. Mas eu utilizei o SQRT(Raiz quadrada)
import math

numero = int(input('Digite um valor: '))
print('Analisando o valor {} \nseu dobro é {} \nseu triplo é {} \nsua raiz quadrada é {:.1f}'.format(numero, numero * 2, numero * 3, math.sqrt(numero)))

#Segunda Forma
numero = int(input('Digite um valor: '))
print('Analisando o valor {} \nseu dobro é {} \nseu triplo é {} \n sua raiz quadrada é {:.1f}'.format(numero, numero * 2, numero * 3, numero ** (1/2)))

#DESAFIO 007 DO CURSO EM VÍDEO PHYTON

n1 = float(input('Nota da primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
print('A média entre {} e {} é igual {:.1f}'.format(n1, n2, (n1 + n2) / 2))

#DESAFIO 008 DO CURSO EM VÍDEO PHYTON

metros = float(input('Distância em metros: '))
print('A medida {} corresponde a'.format(metros))
print('{}KM'.format(metros / 1000))
print('{}HM'.format(metros / 100))
print('{}dam'.format(metros / 10))
print('{:.1f}DM'.format(metros * 10))
print('{:.1f}CM'.format(metros * 100))
print('{:.1f}MM'.format(metros * 1000))

#DESAFIO 009 DO CURSO EM VÍDEO PHYTON


#Primeiro Forma, mas haverá muitas linhas de código

tabuada = int(input('Digite um numero para sua tabuada: '))
print('-' * 20)
print('{} X 1 = {}'.format(tabuada, tabuada  * 1))
print('{} X 2 = {}'.format(tabuada, tabuada * 2))
print('{} X 3 = {}'.format(tabuada, tabuada * 3))
print('{} X 4 = {}'.format(tabuada, tabuada * 4))
print('{} X 5 = {}'.format(tabuada, tabuada * 5))
print('{} X 6 = {}'.format(tabuada, tabuada * 6))
print('{} X 7 = {}'.format(tabuada, tabuada * 7))
print('{} X 8 = {}'.format(tabuada, tabuada * 8))
print('{} X 9 = {}'.format(tabuada, tabuada * 9))
print('{} X 10 = {}'.format(tabuada, tabuada * 10))
print('-' * 20)

#Segunda Forma, mas a linha codígo para executar é extensa

tabuada = int(input('Digite um numero para a sua tabuada: '))
print('A tabuada do seu numero é: {} {} {} {} {} {} {} {} {} {}'.format(tabuada * 1, tabuada * 2, tabuada * 3, tabuada * 4, tabuada * 5, tabuada * 6, tabuada * 7, tabuada * 8, tabuada * 9, tabuada * 10))

#DESAFIO 010 DO CURSO EM VÍDEO PHYTON

carteira = float(input('Quanto dinheiro você tem na carteira?: '))
print('Com R${:.2f} você pode comprar U${:.2f}'.format(carteira, carteira / 5.69))
print('Com R${:.2f} você pode comprar Euro${:.2f}'.format(carteira, carteira / 6.49))

#DESAFIO 011 DO CURSO EM VÍDEO PHYTON

largura = float(input('Largura: '))
altura = float(input('Altura: '))
print('Sua parede tem dimensão {}x{} e sua área é de {}m(^2)'.format(largura, altura, largura * altura))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(largura * altura / 2))

#DEASFIO 012 DO CURSO EM VÍDEO PHYTON


  #Primeira Forma mais direto
preco = float(input('Qual é o preço do produto? '))
print('O produto que custava R${:.2f}, na promoção com desconto 5% vai custar R${:.2f}'.format(preco, preco - (preco * 5 / 100)))

  #Segunda Forma com a variavel desconto
preco = float(input('Qual é o preço do produto? '))
desconto = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, desconto))

#DESAFIO 013 DO CURSO EM VÍDEO PHYTON


  #Primeira forma mais direto
salario = float(input('Digite o salário do funcionário? '))
print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario, salario + (salario * 15 / 100)))

  #Segunda Forma com variavel aumento
salario = float(input('Digite o salário do funcionário? '))
aumento = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario, aumento))

#DESAFIO 014 DO CURSO EM VÍDEO PHYTON

#Primeira Forma
c = float(input('Informa a temperatura em Celsius: '))
F = (c * 1.8 + 32)
print('A temperatura de {} Celsius, em fahrenheit é {}'.format(c, F))

#Segunda Forma
c = float(input('Informa a temperatura em Celsius: '))
print('A temperatura de {} Celsius, em fahrenheint é {}'.format(c, c * 1.8 + 32))

#DESAFIO 015 DO CURSO EM VÍDEO PHYTON

#Primeira Forma
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
print('O total a pagar é R${:.2f}'.format(dias * 60 + km * 0.15))

#Segunda Forma com variável
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = dias * 60 + km * 0.15
print('O total a pagar é R${:.2f}'.format(total))

#DESAFIO 016 DO CURSO EM VÍDEO PHYTON

from math import floor
numero = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, floor(numero)))

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

#DESAFIO 019 DO CURSO EM VÍDEO PHYTON

import random

a1 = str(input('Digite o primeiro aluno: '))
a2 = str(input('Digite o segundo aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Digite o quarto aluno: '))
lista = [a1, a2, a3, a4]
print('O aluno escolhido foi {}'.format(random.choice(lista)))

#DESAFIO 020 DO CURSO EM VÍDEO PHYTON

from random import shuffle
a1 = str(input('Digite o primeiro aluno: '))
a2 = str(input('Digite o segundo aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Digite o quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação é \n{}'.format(lista))

#DESAFIO 021 DO CURSO EM VÍDEO PHYTON

from pygame import mixer

mixer.init()
mixer.music.load('bby.mp3')
mixer.music.play()
input()
mixer.event.wait()

#DESAFIO 022 DO CURSO EM VÍDEO PHYTON

nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome {} tem {} letras'.format(nome.split()[0], len(nome.split()[0])))

#DESAFIO 023 DO CURSO EM VÍDEO

numero = int(input('Informe um número: '))
print('Analisando esse numero {}'.format(numero))
print('Unidade: {}'.format(numero // 1 % 10))
print('Dezena: {}'.format(numero // 10 % 10))
print('Centena: {}'.format(numero // 100 % 10))
print('Milhar: {}'.format(numero // 1000 % 10))

#DESAFIO 024 DO CURSO EM VÍDEO

cidade = str(input('Em que cidade você nasceu? ')).strip()
print('{}'.format(cidade[:5].upper() == 'SANTO'))

#DESAFIO 025 DO CURSO EM VÍDEO

nome = str(input('Qual seu nome completo? ')).upper().strip()
print('Seu nome tem SILVA? {}'.format('SILVA' in nome))

#DESAFIO 026 DO CURSO EM VÍDEO

frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" aparece {} vezes na frase "{}".'.format(frase.lower().count('a'), frase))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.lower().find('a')+1))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.lower().rfind('a')+1))

#DESAFIO 027 DO CURSO EM VÍDEO

nome = str(input('Digite seu nome completo: ')).strip()
print('Prazer em te conhecer! ')
dividido = nome.split()
print('Seu primeiro nome é: {}'.format(dividido[0]))
print('Seu ultimo nome é: {}'.format(dividido[-1]))

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

#DESAFIO 029 DO CURSO EM VÍDEO

velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('Você será multado por R${:.2f}, por estar {:.0f}Km/h acima dos 80KM/h'.format((velocidade - 80) * 7, velocidade - 80))
else:
    print('Tenha um bom dia! Diriga com Segurança')

#DESAFIO 030 DO CURSO EM VÍDEO

numero = int(input('Digite um numero qualquer: '))

if numero % 2 == 0:
    print('Esse numero {} é PAR'.format(numero))
else:
    print('Esse número {} é IMPAR'.format(numero))

#DESAFIO 031 DO CURSO EM VÍDEO

viagem = float(input('Qual a distância da viagem? '))
print('Você está preste a fazer uma viagem de {}KM'.format(viagem))

if viagem  <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(viagem * 0.50))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(viagem * 0.45))

#DESAFIO 032 DO CURSO EM VÍDEO

from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
  ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))

#DESAFIO 033 DO CURSO EM VÍDEO

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

if n1 > n2 and n1 > n3:
    print('O maior valor é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior valor é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior valor é {}'.format(n3))
elif n1 < n2 and n1 < n3:
    print('O menor valor é {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor valor é {}'.format(n2))
elif n3 < n1 and n3 < n2:
    print('O menor valor é {}'.format(n3))

#DESAFIO 034 DO CURSO EM VÍDEO

salario = float(input('Qual o valor do salário do funcionário? R$ '))

if salario > 1250.00:
    print('Quem ganhava R${}, passa a ganhar R${}'.format(salario, salario * 1.10))
else:
    print('Quem ganhava R${}, passa a ganhar R${}'.format(salario, salario * 1.15))

#DESAFIO 035 DO CURSO EM VÍDEO

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('O triângulo existe.')
else:
    print('O triângulo não existe')




