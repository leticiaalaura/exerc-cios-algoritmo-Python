lista  = []

for n in range(3):
  n = int(input('Digite um numero inteiro:'))
  lista.append(n)

print()
lista.sort(reverse=True)
print(lista)
