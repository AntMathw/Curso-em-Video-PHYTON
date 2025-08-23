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
        break

usuário = input('Você quer continuar? [S/N] ')
if usuário.lower() == 's':

        sim = int(input('Digite um número e vê seu numéro por extenso: '))
        valores = ("zero", 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
                   'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                   'dezenove', 'vinte')
    
while True:
        if sim <= 20:
            print(f'Você digitou o numéro {valores[sim]}')
            break
        else:
            print(f'Você digitou o número fora da tupla {sim}')
            break
