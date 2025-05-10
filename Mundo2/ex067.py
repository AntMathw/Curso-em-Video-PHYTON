#DESAFIO 067 DO CURSO EM VÍDEO PHYTON

while True:
    
    valor = int(input('Digite um valor e mostre sua tabuada: '))
    print('=-='*30)
    if valor < 0:
        break
    for c in range(1, 11):
        print(f'{valor} x {c} = {valor*c}')
    print('=-='*30)

print('Programa encerrado, você digitou um número negativo')
