#DESAFIO 050 DO CURSO EM VÍDEO PHYTON

soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('A soma dos numeros pares é {}, e possui {} pares'.format(soma, cont))
