#DESAFIO 070 DO CURSO EM VÍDEO PHYTON

total = totalmil = menor = contador = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    contador += 1
    total += preço
    if preço >= 1000:
        totalmil += 1
    if contador == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total das compras foi: R${total:.2f}')
print(f'Temos {totalmil} produto(s) custando mais de R$1000,00 reais.')
print(f'O produto com o menor preço foi o/a {barato}, que custa R${menor:.2f}')
print('Programa encerrado!')
