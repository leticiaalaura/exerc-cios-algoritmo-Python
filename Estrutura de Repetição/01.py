nota = float(input('Digite uma nota de 0 - 10: '))

while nota < 0 or nota > 10:
  print('Valor inválido')
  nota = float(input('Digite uma nota de 0 - 10: '))
  if nota <= 10:
    print('Valor válido')
    break