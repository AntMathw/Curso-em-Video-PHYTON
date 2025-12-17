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

# Título para deixar bonitinho
print('-=' * 20)
print('   ANALISADOR DE EMPRÉSTIMOS   ')
print('-=' * 20)

# Entrada de dados
casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Salário do comprador? R$ '))
anos = int(input('Em quantos anos ele vai pagar? '))

# Processamento
prestacao = casa / (anos * 12)
minimo = salario * 0.30  # O limite é 30% do salário

# Saída de dados formatada com f-string
print(f'\nPara pagar uma casa de R$ {casa:.2f} em {anos} anos,')
print(f'a prestação será de R$ {prestacao:.2f}.')
print(f'O limite de 30% do seu salário é R$ {minimo:.2f}.')

# Lógica de decisão
if prestacao <= minimo:
    print('\n\033[1;32m✅ Empréstimo CONCEDIDO!\033[m')
else:
    print('\n\033[1;31m❌ Empréstimo NEGADO!\033[m')
    print('A parcela excede 30% do seu salário.')
