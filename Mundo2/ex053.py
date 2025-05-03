#DEASFIO 053 DO CURSO EM VÍDEO PHYTON

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
j = ''.join(palavras)
inv = ''
for letra in range(len(j) - 1, - 1, - 1):
    inv += j[letra]
if inv == j:
    print('É políndromo.')
else:
    print('Não é políndromo.')
