#DESAFIO 036 DO CURSO EM VÍDEO

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Salário do comprador?  '))
ano = int(input('Quantos anos ele vai pagar? '))
emprestimo = casa / (ano * 12)
pmensal = emprestimo * 100 / salario
print('Para pagar uma casa de R${} em {:.0f} anos, a prestação será de R${:.2f}'.format(casa, ano, emprestimo, pmensal))

if emprestimo <= 0.30 * salario:
    print('\033[1;32mEmpréstimo CONCEDIDO!\033[m ')
elif emprestimo > 0.30 * salario:
    print('\033[1;31mEmpréstimo NEGADO!\033[m ')
