a = str(input('Digite o valor do lado A do triangulo: '))
b = str(input('Digite o valor do lado B do triangulo: '))
c = str(input('Digite o valor do lado C do triangulo: '))

if a < b + c and b < a + c and c < a + b:
  print('Os valores podem formar um Triângulo.')
  if a == b == c:
    print('Equilátero')
elif a != b != c != a:
  print('Escaleno')
else:
  print('Isósceles')
