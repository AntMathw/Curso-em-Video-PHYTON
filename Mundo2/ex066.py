#DESAFIO 066 DO CURSO EM VÍDEO PHYTON

n = cont = soma = 0
cont = 0
while True:
    n = int(input('Digite um valor[999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} os números é {soma}')
