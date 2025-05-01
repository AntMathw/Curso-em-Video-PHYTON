#DESAFIO 029 DO CURSO EM VÍDEO

velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('Você será multado por R${:.2f}, por estar {:.0f}Km/h acima dos 80KM/h'.format((velocidade - 80) * 7, velocidade - 80))
else:
    print('Tenha um bom dia! Diriga com Segurança')

