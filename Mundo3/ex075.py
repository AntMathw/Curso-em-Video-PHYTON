# Parte do código em que o usuário digita 4 valores
numbers = (int(input('Digite um número: ')),
            int(input('Digite segundo número: ')),
            int(input('Digite outro valor: ')),
            int(input('Digite o último número: ')))
# Valores guardados em uma váriavel de elementos
element = numbers
# Imprime quais números o usuário digitalizou
print(f'Você digitou os números {element}')
# Imprime no console quantas vezes apareceu o número nove
print(f'O número 9 apareceu {numbers.count(9)} vezes')
# Linha do código em que usa a estrutura IF caso o usuário digitou o número 3
if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3)} posição')
# Else utilizado caso não tenha nenhum número 3 na tupla
else:
    print('O valor 3 não foi digitado em nenhuma das posições')
# Bloco em que mostra quais números são pares. Ou seja divisível por 2 % 0
print(f'O valores pares são ', end='')

for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')


