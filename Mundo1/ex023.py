#DESAFIO 023 DO CURSO EM VÍDEO

numero = int(input('Informe um número: '))
print('Analisando esse numero {}'.format(numero))
print('Unidade: {}'.format(numero // 1 % 10))
print('Dezena: {}'.format(numero // 10 % 10))
print('Centena: {}'.format(numero // 100 % 10))
print('Milhar: {}'.format(numero // 1000 % 10))
