#DESAFIO 015 DO CURSO EM VÍDEO PHYTON

#Primeira Forma
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
print('O total a pagar é R${:.2f}'.format(dias * 60 + km * 0.15))

#Segunda Forma com variável
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = dias * 60 + km * 0.15
print('O total a pagar é R${:.2f}'.format(total))
