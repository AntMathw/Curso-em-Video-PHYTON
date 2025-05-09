#DESAFIO 063 DO CURSO EM VÍDEO PHYTON

print('=-='*30)
print('Sequência de Fibonacci')
print('=-='*30)

termo = int(input('Quantos termos deseja mostrar? '))
n1 = 0
n2 = 1
print('~'*30)
print('{} => {}'.format(n1, n2), end='')

cont = 3
while cont <= termo:
    n3 = n1 + n2
    print(' => {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1
print(' => FIM')
print('~'*30)
