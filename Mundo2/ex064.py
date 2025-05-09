#DESAFIO 064 DO CURSO EM VÍDEO PHYTON

num = cont = soma = 0
num = int(input('Digite um número [999 para parar o programa]: '))
while num!= 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar o programa]: '))
print('VocÊ digitou tantos números {}, o resultado entre eles é {}'.format(cont, soma))
print('FIM')

