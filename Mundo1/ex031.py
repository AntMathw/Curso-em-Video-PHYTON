#DESAFIO 031 DO CURSO EM VÍDEO

viagem = float(input('Qual a distância da viagem? '))
print('Você está preste a fazer uma viagem de {}KM'.format(viagem))

if viagem  <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(viagem * 0.50))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(viagem * 0.45))
