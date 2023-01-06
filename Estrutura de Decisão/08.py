a = float(input('Qual o valor do item 1? '))
b = float(input('Qual o valor do item 2? '))
c = float(input('Qual o valor do item 3? '))

menor = a
if b < a and  b < c:
  menor = b
if c < a and c < b:
  menor = c
print(f'Você deverá optar pelo item de {menor} porque é mais barato.')