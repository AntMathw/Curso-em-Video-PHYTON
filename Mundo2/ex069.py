#DESAFIO 069 DO CURSO EM VÍDEO PHYTON

print('-'*30)
print('    CADASTRO DE UMA PESSOA      ')
print('-'*30)

pessoas18 = totH = totF20 = 0

while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        pessoas18 += 1
    if sexo == 'M':
        totH += 1
    elif sexo == 'F' and idade < 20:
        totF20 += 1
    final = ' '
    
    while final not in 'SN':
        final = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if final == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {pessoas18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E no cadasto há {totF20} mulheres com menos de 20 anos')

