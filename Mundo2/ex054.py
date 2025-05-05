#DESAFIO 054 DO CURSO EM VÍDEO PHYTON

from datetime import date

menor = 0
maior = 0

for idade in range(0, 7):
  nascimento = int(input('Digite o ano de nascimento: '))
    idade2 = date.today().year - nascimento
    if idade2 >= 18:
        maior += 1
    else:
        menor += 1
print('De 7 pessoas {} são jovens e {} pessoas são mais velhos'.format(menor, maior))
