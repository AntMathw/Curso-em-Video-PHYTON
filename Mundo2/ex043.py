#DESAFIO 043 DO CURSO EM VÍDEO PHYTON

peso = float(input('Qual é seu peso? '))
altura = float(input('Qual sua altura? '))
IMC = peso / (altura * altura)

if IMC < 18.5:
    print('Seu IMC {:.1f}, está abaixo do peso.'.format(IMC))
elif IMC == 18.5 or IMC < 25:
    print('Seu IMC {:.1f}, está no peso ideal.'.format(IMC))
elif IMC == 25 or IMC == 30:
    print('Seu IMC {:.1f}, está em sobrepeso'.format(IMC))
elif IMC > 30 or IMC < 40:
    print('Seu IMC {:.1f}, está em caso de OBESIDADE'.format(IMC))
elif IMC > 40:
    print('Seu IMC {:.1f}, está em caso de OBESIDADE MÓRBIDA'.format(IMC))

