nota = float(input('Informe a nota da aluna: '))
frequencia = float(input('Informe a frequência da aluna: '))

if 7 <= nota <= 10 and 75 <= frequencia <= 100:
    print('Aprovada')
elif 1 < nota < 7 or 0 < frequencia < 75:
    print('Reprovada')
else:
    print('Nota inválida')