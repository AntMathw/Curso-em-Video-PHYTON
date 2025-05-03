#DESAFIO 052 DO CURSO EM VÍDEO PHYTON

num = int(input('Digite um número: '))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[34m', end='')
        total += 1

    else:
        print('\033[m', end='')
    print('{} '.format(i), end='')
if total == 2:
    print('\n\033[mÉ um número primo.')
else:
    print('\n\033[mEsté número não é primo.')
