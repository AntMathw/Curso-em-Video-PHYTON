#DESAFIO 008 DO CURSO EM VÍDEO PHYTON

metros = float(input('Distância em metros: '))
print('A medida {} corresponde a'.format(metros))
print('{}KM'.format(metros / 1000))
print('{}HM'.format(metros / 100))
print('{}dam'.format(metros / 10))
print('{:.1f}DM'.format(metros * 10))
print('{:.1f}CM'.format(metros * 100))
print('{:.1f}MM'.format(metros * 1000))
