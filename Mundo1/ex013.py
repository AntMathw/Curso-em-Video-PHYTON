#DESAFIO 013 DO CURSO EM VÍDEO PHYTON


  #Primeira forma mais direto
salario = float(input('Digite o salário do funcionário? '))
print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario, salario + (salario * 15 / 100)))

  #Segunda Forma com variavel aumento
salario = float(input('Digite o salário do funcionário? '))
aumento = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario, aumento))

#OUTRA FORMA MAIS AVANÇADA

def calcular_novo_salario(salario_base, percentual_aumento):
    """
    Calcula o novo salário de um funcionário após um aumento percentual.

    Args:
        salario_base (float): O salário original do funcionário.
        percentual_aumento (float): A taxa de aumento (ex: 15 para 15%).

    Returns:
        float: O novo valor do salário após o aumento.
    """
    # Converte a porcentagem (ex: 15) para um fator decimal (ex: 0.15)
    fator_aumento = percentual_aumento / 100
    
    # Calcula o novo salário de forma eficiente (salario * 1.15 para 15%)
    novo_salario = salario_base * (1 + fator_aumento)
    
    return novo_salario

def main():
    """
    Função principal que gerencia a interação com o usuário.
    """
    print("=" * 40)
    print("CALCULADORA DE AUMENTO SALARIAL")
    print("=" * 40)

    try:
        # Obter o salário do usuário com tratamento de erro
        salario = float(input('Digite o salário atual do funcionário (R$): '))
        
        # Obter a porcentagem de aumento (o código original usava 15%, mas agora é flexível)
        percentual = float(input('Digite o percentual de aumento desejado (ex: 15): '))
        
        # Executar a função de cálculo
        novo_salario = calcular_novo_salario(salario, percentual)
        
        # Exibir o resultado formatado
        print("\n--- Resultado do Cálculo ---")
        print('Salário Original: R${:.2f}'.format(salario))
        print('Percentual de Aumento: {:.2f}%'.format(percentual))
        
        # Uso da variável 'novo_salario' no final, mantendo a estrutura da sua segunda forma
        print('Um funcionário que ganhava R${:.2f}, com aumento de {:.2f}%, passa a receber R${:.2f}'.format(
            salario, percentual, novo_salario
        ))
        print("----------------------------")

    except ValueError:
        # Mensagem de erro se o usuário não digitar um número
        print("\n❌ ERRO: Por favor, digite apenas valores numéricos válidos (ex: 1500.00 ou 15).")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
