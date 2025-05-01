#DESAFIO 041 DO CURSO EM VÍDEO

from datetime import date

idade = int(input('Digite sua idade ou ano de nascimento: '))
anoatual = date.today().year
subtrai = anoatual - idade

if idade <= 9 or subtrai <= 9:
    print('Categoria será MIRIM.')
elif idade <= 14 or subtrai <= 14:
    print('Cateoria será INFANTIL.')
elif idade <= 19 or subtrai <= 19:
    print('Categoria será JÚNIOR.')
elif idade <= 25 or subtrai <= 25:
    print('Categoria será SÊNIOR.')
elif idade > 25:
    print('Categoria será MASTER.')
