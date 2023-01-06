morango = float(input('Digite a quantidade de morango em kg: '))
maca = float(input('Digite a quantidade de maçã em kg: '))
total_kg = morango + maca
preco_morango = 2.50
preco_maca = 1.80
desconto  = 0.10

# Morango
if morango <= 5:
  preco_total_morango = morango * preco_morango
elif morango > 5 or morango < 8:
  preco_total_morango = (preco_morango - 0.30) * morango
# Maçã
if maca <= 5:
  preco_total_maca = maca * preco_maca
elif maca > 5 or maca < 8:
  preco_total_maca = (preco_maca - 0.30) * maca

preco_total_final = preco_total_morango + preco_total_maca
print(f'A quantidade de morango e de maçãs adquiridas é de {total_kg}kg por R${preco_total_final}')

if preco_total_final > 25:
  desconto_por_preco = preco_total_final * desconto
  final_desconto = preco_total_final - desconto_por_preco
  print(f'Compra ultrapassou R$25 reais desconto de 10% concedido. Valor total a pagar é de R${final_desconto} reais.')
elif total_kg >= 16:
  desconto_por_kg = preco_total_final * desconto
  final_desconto = preco_total_final - desconto_por_kg
  print(f'Compra ultrapassou 16Kg e o desconto de 10% foi concedido. Valor total a pagar é de R${final_desconto} reais')