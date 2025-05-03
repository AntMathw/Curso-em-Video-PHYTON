#DESAFIO 051 DO CURSO EM VÍDEO PHYTON

print('=' * 35)
print('TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('=' * 35)

primeiro = int(input('Digite o pimeiro termo: '))
razao = int(input('Digite a razão: '))

for i in range(0 , 10):
    print(primeiro + (razao * i), end=' ')
print('FIM')
