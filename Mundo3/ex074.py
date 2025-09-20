# Adicionamos alguns números dentro da tupla
numeros_na_tupla = (10, 44, 53, 2, 3, 5, 634534, 231234, 53445)

# Bloco para verificar se a tupla não está vazia
if numeros_na_tupla:
    # Usamos a função embutida "max()" para encontrar o maior valor.
    maior_numero = max(numeros_na_tupla)
    
    # Usamos a função embutida "min()" para encontrar o menor valor.
    menor_numero = min(numeros_na_tupla)
    
    # Executamos para que mostra no output(saída)
    print(f"A tupla é: {numeros_na_tupla}")
    print(f"O maior número na tupla é: {maior_numero}")
    print(f"O menor número na tupla é: {menor_numero}")
else:
    # Caso a tupla esteja vazia, mostramos uma mensagem.
    print("A tupla está vazia. Não é possível encontrar o maior ou menor número.")

