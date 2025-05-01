#DESAFIO 040 DO CURSO EM VÍDEO

prova1 = float(input('Nota da primeia prova: '))
prova2 = float(input('Nota da segunda prova: '))
resultado = (prova1 + prova2) / 2

if resultado >= 7:
    print('A nota {} e {}, a média do aluno vai ser {}\n\033[1;36mAPROVADO\033[m'.format(prova1, prova2, resultado))
elif resultado < 5.0:
    print('A nota {} e {}, a média do aluno vai ser {}\n\033[1;31mREPROVADO\033[m'.format(prova1, prova2, resultado))
elif resultado == 5.9 or 6.9:
    print('A nota {} e {}, a média do aluno vai ser {}\nRECUPERAÇÃO'.format(prova1, prova2, (resultado)))
