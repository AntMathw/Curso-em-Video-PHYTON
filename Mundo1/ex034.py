#DESAFIO 034 DO CURSO EM VÍDEO

salario = float(input('Qual o valor do salário do funcionário? R$ '))

if salario > 1250.00:
    print('Quem ganhava R${}, passa a ganhar R${}'.format(salario, salario * 1.10))
else:
    print('Quem ganhava R${}, passa a ganhar R${}'.format(salario, salario * 1.15))
