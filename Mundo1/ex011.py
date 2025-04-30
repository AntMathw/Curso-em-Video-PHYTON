#DESAFIO 012 DO CURSO EM VÍDEO PHYTON


  #Primeira Forma mais direto
preco = float(input('Qual é o preço do produto? '))
print('O produto que custava R${:.2f}, na promoção com desconto 5% vai custar R${:.2f}'.format(preco, preco - (preco * 5 / 100)))

  #Segunda Forma com a variavel desconto
preco = float(input('Qual é o preço do produto? '))
desconto = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, desconto))

