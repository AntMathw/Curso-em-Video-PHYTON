#DESAFIO 048 DO CURSO EM VÍDEO PHYTON

cont = 0
soma = 0
for impar in range(3, 501, 3):
    if impar % 2 == 1:
        cont += impar
        soma += 1

print('A soma é {} e o numero de valores é {}'.format(soma, cont, end=' '))

