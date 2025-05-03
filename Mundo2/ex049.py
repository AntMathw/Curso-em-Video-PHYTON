#DESAFIO 049 DO CURSO EM VÍDEO PHYTON

num = int(input('Digite um número e veja sua tabuada: '))
for vezes in range(1, 11):
    final = num * vezes
    print('{} x {} = {}'.format(num, vezes, final))

