#DESAFIO 042 DO CURSO EM VÍDEO

r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))
if (r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r2 == r3 and r2 != r1):
    print('Seu triangulo pode se um ISOSCELES, possui dois lados iguis mas um é diferente')
elif r1 == r2 == r3:
    print('Seu triangulo pode ser um EQUILATERO, possui todos lados iguais')
elif r1 != r2 != r3 and r2 != r1 != r3 and r3 != r1 != r2:
    print('Seu triangulo pode ser um ESCALENO, possui todos lados diferentes')
