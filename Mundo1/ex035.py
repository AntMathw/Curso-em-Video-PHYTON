#DESAFIO 035 DO CURSO EM VÍDEO

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('O triângulo existe.')
else:
    print('O triângulo não existe')

#EXEMPLO DETALHADO

# 1. Coletando os comprimentos
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

# 2. Organizando as retas e simplificando a verificação
# 'sorted' coloca os valores em ordem crescente
retas = sorted([r1, r2, r3])

# Desempacotamento: a é o menor lado, c é o maior
a, b, c = retas 

# 3. Verificando a Condição de Existência
# Pela matemática, basta checar se a soma dos dois menores lados (a+b)
# é maior que o lado maior (c). As outras duas condições são garantidas.
if a + b > c:
    print('\n✅ **O triângulo PODE SER FORMADO.**')
    
    # 4. Classificando o Tipo de Triângulo
    if a == c:  # Se a=b e b=c, basta checar a==c
        print('Tipo: **EQUILÁTERO** (Todos os lados iguais).')
    elif a == b or b == c:
        print('Tipo: **ISÓSCELES** (Dois lados iguais).')
    else:
        print('Tipo: **ESCALENO** (Todos os lados diferentes).')

else:
    print('\n❌ **O triângulo NÃO PODE SER FORMADO.**')
    print('Regra: A soma de dois lados deve ser maior que o terceiro lado.')
