#DESAIO 065 DO CURSO EM VÍDEO PHYTON

resposta = 'S'
soma = quant = media = maior = menor = 0
while resposta in 'SIMsimSs':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / num
print('Você digitou {} números e a média foi {:.2f}.'.format(num, media))
print('O maior valor foi {} e o menor {}.'.format(maior, menor))

