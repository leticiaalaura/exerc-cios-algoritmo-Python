n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
operacao = input('Digite com caracteres qual operação deseja realizar: ')

if operacao == '+':
  resultado = n1 + n2
  print(resultado)
elif operacao == '-':
  resultado = n1 - n2
  print(resultado)
elif operacao == '/':
  resultado = n1 / n2
  print(resultado)
elif operacao == '*':
  resultado = n1 * n2
  print(resultado)
else:
  print('Operação não identificada.')

# Par ou ímpar:
if resultado % 2 == 0:
  print('Número par')
else:
  print('Número ímpar')

# Positivo ou negativo:
if resultado <= 0:
  print('Número negativo ')
else:
  print('Número positivo')

# Inteiro ou decimal
if resultado % 1 == 0:
  print('Numero inteiro')
else:
  print('Numero decimal')