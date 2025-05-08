#DESAFIO 061 DO CURSO EM VÍDEO PHYTON

print('Gerador de PA')
print('=-=' * 6)
pa = int(input('Primeiro Termo: '))
r = int(input('Digite a razão: '))

termo = pa
c = 1

while c <= 10:
    print('{} => '.format(termo), end=' ')
    termo += r
    c += 1
print('FIM')


