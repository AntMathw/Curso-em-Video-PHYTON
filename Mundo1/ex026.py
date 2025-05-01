#DESAFIO 026 DO CURSO EM VÍDEO

frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" aparece {} vezes na frase "{}".'.format(frase.lower().count('a'), frase))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.lower().find('a')+1))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.lower().rfind('a')+1))
