a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
# Verificando o maior
maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c
print(f'O maior numero é {maior}')