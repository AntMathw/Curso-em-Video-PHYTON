#DESAFIO 044 DO CURSO EM VÍDEO PHYTON

print('{:.^40}'.format(' Lojas Sousa '))
preco = float(input('Digite o preço do produto: '))
forma = int(input('Escolha o método de pagamento:\n[ 1 ] - À vista. 5% de desconto.\n[ 2 ] - Em até 2x'
                   ' no cartão. Preço formal.\n[ 3 ] - 3x ou mais no cartão. 20% de juros.'
                   '\nDigite aqui: '))
if forma == 1:
    print('O valor do produto receberá 5% de desconto, totalizando: R${:.2f}'.format(preco * 0.95))
elif forma == 2:
    print('O valor do produto poderá ser parcelado em 2 vezes sem alteração no valor'
          ' ,totalizando: R${:.2f} e cada parcela custando: R${:.2f}'.format(preco, preco/2))
else:
    nvezes = int(input('Digite o número de parcelas (minímo: 3, máximo: 12): '))
    if nvezes < 3 or nvezes > 12:
        print('Tal número de meses \033[1;31mNÂO\033[m é permitido!')
    else:
        print('O valor do produto será parcelado em {} vezes, o preço total sofrerá juros de'
              ' 20%, fazendo com que cada parcela custe: R${:.2f}, \ne o total a ser pago: R${:.2f}'
              .format(nvezes, (preco / nvezes) * 1.2, preco * 1.2))
