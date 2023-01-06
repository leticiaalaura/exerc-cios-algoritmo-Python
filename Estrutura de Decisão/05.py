nota_1 = float(input('Digite a nota: '))
nota_2 = float(input('Digite a nota: '))
media = (nota_1 + nota_2) / 2

if media == 10:
    print('Aprovado(a) com distinção')
elif media >= 7:
    print('Aprovado(a)')
else:
    print('Reprovado(a)')

