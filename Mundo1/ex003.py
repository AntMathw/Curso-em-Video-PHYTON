#DESAFIO 003 DO CURSO EM VÍDEO PHYTON

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor:: '))
print('A soma entre {} e {} é igual a {}'.format(num1, num2, num1+num2))

#MAIS UM EXEMPLO

# Este programa solicita ao usuário dois valores inteiros,
# calcula a soma entre eles e exibe o resultado formatado.

# 1. Solicita o primeiro valor ao usuário.
# A função 'input()' sempre retorna uma string, por isso usamos 'int()'
# para converter a entrada para um número inteiro.
num1 = int(input('👉 Por favor, digite o primeiro número inteiro: '))

# 2. Solicita o segundo valor ao usuário.
num2 = int(input('👉 Agora, digite o segundo número inteiro: '))

# 3. Realiza o cálculo da soma e armazena o resultado em uma nova variável.
resultado_soma = num1 + num2

# 4. Exibe o resultado final de forma mais descritiva.
# Usamos o método .format() para inserir os valores nas chaves {}.
print('-' * 40) # Linha de separação para melhorar a visualização
print('✅ Detalhes da Operação:')
print('   - Primeiro valor fornecido: {}'.format(num1))
print('   - Segundo valor fornecido: {}'.format(num2))
print('   - O cálculo realizado foi: {} + {} = {}'.format(num1, num2, resultado_soma))
print('---')
print('**A soma final entre {} e {} é igual a {}!**'.format(num1, num2, resultado_soma))
print('-' * 40)
