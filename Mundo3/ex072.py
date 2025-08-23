#Tuplas número em extenso

num = int(input('Digite um número de 0 a 20: '))
numero = ("zero", "um", "dois", "três", "quatro"
          , "cinco", "seis", "sete", "oito", "nove", 
          "dez", "onze", "doze", "treze", "quatorze", ""
          "quinze", "dezesseis", "dezessete", "dezoito", 
          "dezenove", "vinte")
if num  <= 20:
    print(f'Você digitou o número {numero[num]}')
elif num > 20:
    print('Você digitou um número fora da tupla')

#Segunda forma de número em extenso

num = int(input('Digite um número de 0 a 20: '))
numero = ("zero", "um", "dois", "três", "quatro"
          , "cinco", "seis", "sete", "oito", "nove", 
          "dez", "onze", "doze", "treze", "quatorze", ""
          "quinze", "dezesseis", "dezessete", "dezoito", 
          "dezenove", "vinte")
while True:
    if num  <= 20:
        print(f'Você digitou o número {numero[num]}')
        break
    elif num > 20:
        print('Você digitou um número fora da tupla')
