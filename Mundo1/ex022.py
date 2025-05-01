#DESAFIO 022 DO CURSO EM VÍDEO PHYTON

nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome {} tem {} letras'.format(nome.split()[0], len(nome.split()[0])))

