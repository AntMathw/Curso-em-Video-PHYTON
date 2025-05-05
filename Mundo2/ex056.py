#DESAFIO 05 DO CURSO EM VÍDEO PHYTON

somaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulheres = 0

for p in range(1, 5):
    print('==' * 14)
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Digite o sexo da {}ª pessoa: [M/F] '.format(p))).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulheres += 1
media = somaidade / 4

print('A média de idade das 4 pessoas é de {} anos.'.format(media))
print('A idade do homem mais velho é de {} e o seu nome é {}.'.format(maioridadehomem, nomevelho))
if totalmulheres >= 2:
    print('No total, existem {} mulheres com menos de 20 anos.'.format(totalmulheres))
elif totalmulheres == 1:
    print('No total, existe {} mulher com menos de 20 anos.'.format(totalmulheres))
else:
    print('No total, existem {} mulheres com menos de 20 anos.'.format(totalmulheres))
