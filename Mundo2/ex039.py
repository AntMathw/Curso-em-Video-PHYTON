#DESAFIO 039 DO CURSO EM VÍDEO

from datetime import date

nascimento = int(input('Em que ano você nasceu? '))
hoje = date.today().year

if nascimento == hoje:
    print('O ano de {}, você obrigatoriamente tem que se alistar! '.format(date.today().year))
elif hoje - nascimento > 18:
    print('O ano de {}, alistamento ja ocorreu, mas se não se alistou, FAÇA!'.format(nascimento + 18))
else:
    print('O seu alistamento ainda não chegou. Ele vai acontecer em {}'.format(nascimento + 18))

