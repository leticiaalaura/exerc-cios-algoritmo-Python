import math

a = int(input('valor de a: '))
if a == 0:
  print('Não é equação de segundo grau. Tchau')
else:
  b = int(input('valor de b: '))
  c = int(input('valor de c: '))
  delta - b * b - (4 * a * c)
  if delta < 0:
    print('Delta menor que 0. Tchau')
  elif delta == 0:
    raiz = -b / (2 * a)
    print(f'Delta = 0, raiz = {raiz}')
  else:
    raiz1 = (- b + math.sqrt(delta)) / (2 * a)
    raiz2 = (- b - math.sqrt(delta)) / (2 * a)
    print(f'Raizes: {raiz1} e {raiz2}')
