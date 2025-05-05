#DESAFIO 055 DO CURSO EM VÍDEO

menor = 0
maior = 0

for p in range(1, 6):
  peso = float(input('Digite o peso da {} pessoa'.format(p)))
 
  if p == 1:
    peso = maior
    peso = menor
  else:
    if peso > maior:
      peso = maior
    if peso < menor:
      peso = menor

print('Das 5 pessoas, o maior peso é {}KG e o menor peso é {}KG'.format(maior, menor)
  

