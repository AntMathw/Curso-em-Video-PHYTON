#DESAFIO 068 DO CURSO EM VÍDEO PHYTON

from random import randint

print('--'*30)   
print('JOGO DO PAR E ÍMPAR')
print('--'*30)
v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(', deu par!' if total % 2 == 0 else ', deu ímpar!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Parabéns, você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Parabéns, você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente.')
print(f'Fim de jogo! Você venceu {v} vezes!')

