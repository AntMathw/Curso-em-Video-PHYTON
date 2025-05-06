#DESAFIO 057 DO CURSO EM VÍDEO PHYTON

sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe seu sexo sexo novamente')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

