produto = (input('Qual o combustível a ser colocado? Digite  A-álcool, G-gasolina: ')).lower()
litros = float(input('Quantos litros? '))
preco_a = 1.90 * litros
preco_g = 2.5 * litros

# Álcool
if produto == 'a':
  if litros <= 20:
    preco = preco_a - 0.03
  elif litros >= 21:
    preco = preco_a - 0.03
# Gasolina
elif produto == 'g':
  if litros <= 20:
    preco = preco_g - 0.04
  elif litros >= 21:
    preco = preco_g - 0.06
print(f'Será abastecido {litros} de {produto} por {preco}.')