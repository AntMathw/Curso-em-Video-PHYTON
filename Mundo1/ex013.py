#DESAFIO 013 DO CURSO EM VÍDEO PHYTON


  #Primeira forma mais direto
salario = float(input('Digite o salário do funcionário? '))
print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario, salario + (salario * 15 / 100)))

  #Segunda Forma com variavel aumento
salario = float(input('Digite o salário do funcionário? '))
aumento = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario, aumento))

