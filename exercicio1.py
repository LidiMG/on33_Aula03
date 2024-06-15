""" nota = float(input('Digite a nota: '))

def avaliacao(nota):
    nota = float(input('Digite a nota: '))
    return nota

avaliacao()

if nota >= 7 and nota <= 10:
    print('Você foi aprovado!')
elif nota >= 1 and nota < 7:
    print('Você está reprovado.')
elif nota > 10:
    print('Nota inválida. Digite um valor de 1 a 10.')
    return avaliacao();
else:
    print('Nota inválida. Digite um valor de 1 a 10.'); """

while True:
    nota = int(input('Insira uma nota de 1 a 10: '))
    if 1 <= nota <= 10:
        if nota >=7:
            print('Aprovado')
        else:
            print('Reprovado')
        break
    else:
        print('Nota invalida, digite uma nota entre 1 e 10')