nota = int(input("Digite a nota da aluna: "))
presenca = int(input("Digite o número de presenças da aluna: "))
if nota >= 7 and presenca >= 8:
    print('Aprovada')
else:
    print('Reprovada')