nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
media = (nota_1 + nota_2 + nota_3) / 3

if media == 10:
  print(f'A média é {media}. Aprovado com distinção!')
elif media >= 7:
  print(f'A média é {media}. Aprovado(a)!')
elif media < 7:
  print(f'A média é {media}. Reprovado(a)!')
