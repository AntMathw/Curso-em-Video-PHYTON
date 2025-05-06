#DESAFIO 059 DO CURSO EM VÍDEO PHYTON

num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo Valor: '))

opcao = 0
while opcao != 5:
    print('[ 1 ]SOMAR \n[ 2 ]MULTIPLICAR \n[ 3 ]MAIOR \n[ 4 ]NOVOS NÚMEROS \n[ 5 ]SAIR DO PROGRAMA')
    opcao = int(input('>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}'.format(num1, num2, soma))
    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicação entre {} x {} é {}'.format(num1, num2, mult))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior numero entre {} e {} é {}'.format(num1, num2, maior))
    elif opcao == 4:
        print('Informe um número novamente ')
        num1 = int(input('Primeiro Valor: '))
        num2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida, Tente Novamente')
    print('=-=' * 10)



print('Fim do Programa! Ansioso pelo seu retorno!')










