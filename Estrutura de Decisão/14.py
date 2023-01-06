n1 = float(input('Digite a 1ª nota da disciplina: '))
print(f'1ª nota: {n1}')
n2 = float(input('Digite a 2ª nota da disciplina: '))
print(f'2ª nota: {n2}')
media = (n1 + n2) / 2
print(f'Media: {media}')

if media >= 9:
  print('Conceito A')
  print('Aprovado')
elif media >= 7.5:
  print('Conceito B')
  print('Aprovado')
elif media >= 6:
  print('Conceito C')
  print('Aprovado')
elif media >= 4:
  print('Conceito D')
  print('Reprovado')
else:
  print('Conceito E')
  print('Re3provado')