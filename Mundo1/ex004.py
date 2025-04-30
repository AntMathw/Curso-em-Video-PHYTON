#DESAFIO 004 CURSO EM VÍDEO PHYTON


nome = input('Digite algo: ')
print('O tipo primitivo é: ', type(nome))
print('So tem espaços? {}'.format(nome.isspace()))
print('é um número? {}'.format(nome.isnumeric()))
print('É analfabético? {}'.format(nome.isalpha()))
print('É alfanumérico? {}'.format(nome.isalnum()))
print('Está em MAIUSCULO? {}'.format(nome.isupper()))
print('Está em minusculo? {}'.format(nome.islower()))
print('Está capitalizada? {}'.format(nome.istitle()))
