#DESAFIO 060 DO CURSO EM VÍDEO PHYTON

fatorial = int(input('Digite um número \nDescubra o seu fatorial: '))
c = fatorial
print(f'Calculando {c}! = ', end=' ')
f = 1

while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))


