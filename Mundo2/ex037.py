#DESAFIO 037 DO CURSO EM VÍDEO

numero = int(input('Digite um número para ser convertido: '))
escolhido = int(input('Escolha uma conversão: \n[ 1 ]CONVERSOR NÚMERO BINARIO \n[ 2 ]CONVERSOR NÚMERO OCTAL'
                     '\n[ 3 ]CONVERSOR NÚMERO HEXADECIMAL\nDigite aqui: '))
if escolhido == 1:
    print(int(input('A conversão do número {} para binário é {}'.format(numero, bin(numero)[2:]))))
elif escolhido == 2:
    print(int(input('A conversão do numero {} para octal é {}'.format(numero, oct(numero)[2:]))))
elif escolhido == 3:
    print(int(input('A conversão do número {} para hexadecimal é {}'.format(numero, hex(numero)[2:]))))
