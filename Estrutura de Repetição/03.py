# Nome > 3 caracteres
nome = str(input('Informe o nome: '))
while len(nome) <= 3:
  print('INVÁLDO')
  nome = str(input('Informe o nome com mais de 3 caracteres: '))

# Idade <= 150 anos
idade = int(input('Informe a idade: '))
while idade < 0 or idade > 150:
  print('INVÁLDO')
  idade = int(input('Informe a idade: '))

# Salário > 0
salario = float(input('Informe o salário: R$'))
while salario <= 0:
  print('INVÁLDO')
  salario = float(input('Informe o salário: R$'))

# Sexo (F or M)
sexo = str(input('Digite F - Feminino ou M - Masculino: '))
while sexo != 'f' and sexo != 'm':
  print('INVÁLDO')
  sexo = str(input('Digite F - Feminino ou M - Masculino: '))

# Estado civil
civil = str(input('Informe o estado civil: '))
while civil != 'solteiro' and civil != 'casado' and civil != 'divorciado' and civil != 'viuvo':
  print('INVÁLDO')
  civil = str(input('Informe o estado civil: '))