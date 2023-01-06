saque = int(input('Digite o valor do saque: '))

cem = cinquenta = dez = cinco = um = ''


if saque > 600:
  print('Valor acima do limite')
elif saque < 10:
  print('Valor abaixo do limite')
else:
  notas_de_cem, saque = divmod(saque,100)

  if notas_de_cem == 1:
    cem = '1 nota de 100'
  elif notas_de_cem > 1 <= 6:
    cem = f'{notas_de_cem} notas de 100'

  notas_de_cinquenta, saque = divmod(saque,50)

  if notas_de_cinquenta == 1:
    cinquenta = '1 nota de 50'
  elif notas_de_cinquenta > 1:
    cinquenta = f'{notas_de_cinquenta} notas de 50'

  notas_de_dez, saque = divmod(saque,10)

  if notas_de_dez == 1:
    dez =  '1 nota de 10'
  elif notas_de_dez > 1:
    dez = f'{notas_de_dez} notas de 10'

  notas_de_cinco, saque = divmod(saque,5)

  if notas_de_cinco == 1:
    cinco = '1 nota de 5'
  elif notas_de_cinco > 1:
    cinco = f'{notas_de_cinco} notas de 5'

  if saque == 1:
    um = '1 nota de 1'
  elif saque > 1:
    um = f'{saque} notas de 1'

print(cem, cinquenta, dez, cinco, um)