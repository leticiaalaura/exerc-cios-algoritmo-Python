print('Responda as perguntas com S para Sim ou N para Não.')

a = input('Telefonou para a vítima? ')
a.lower() #comando para prevenir caso o usuario digite em CAPSLOCK
count = 0
if a == 's':
  count = count + 1

b = input('Esteve no local do crime? ')
b.lower() #comando para prevenir caso o usuario digite em CAPSLOCK
if b == 's':
  count = count + 1

c = input('Mora perto da vítima? ')
c.lower() #comando para prevenir caso o usuario digite em CAPSLOCK
if c == 's':
  count = count + 1

d = input('Devia para a vítima? ')
d.lower() #comando para prevenir caso o usuario digite em CAPSLOCK
if d == 's':
  count = count + 1

e = input('Já trabalhou com a vítima? ')
e.lower() #comando para prevenir caso o usuario digite em CAPSLOCK
if e == 's':
  count = count + 1

# classificação sobre a participação da pessoa no crime:
if count == 2:
  print('Suspeito(a)')
elif count ==3 or count == 4:
  print('Cúmplice')
elif count == 5:
  print('Assassino(a)')
else:
  print('Inocente')