carne = str(input('Informe o tipo de carne. Opções: Filé Duplo, Alcatra e Picanha: ')).upper()
kilo = float(input('Digite a quantidade em KG: '))

# Filé Duplo
if carne == 'FILÉ DUPLO':
  if kilo <= 5:
    total = kilo * 4.90
  else:
    total = kilo * 5.80
# Alcatra
if carne == 'ALCATRA':
  if kilo <= 5:
    total = kilo * 5.9
  else:
    total = kilo * 6.80
# Picanha
if carne == 'PICANHA':
  if kilo <= 5:
    total = kilo * 6.90
  else:
    total = kilo * 7.80

print(f'{carne}, {kilo}Kg. Preço R${total}')
