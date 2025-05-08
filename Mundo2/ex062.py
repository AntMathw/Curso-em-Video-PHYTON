#DESAFIO 062 DO CURSO EM VÍDEO PHYTON

print('Gerador de PA')
print('=-=' * 6)
pa = int(input('Primeiro Termo: '))
r = int(input('A razão: '))

termo = pa
c = 1
total = 0
continuacao = 10
while continuacao != 0:
    total = total + continuacao
    while c <= total:
        print('{} => '.format(termo), end=' ')
        termo += r
        c += 1
    print('PAUSA')
    continuacao = int(input('Quantos termos você quer mostrar novamente? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
