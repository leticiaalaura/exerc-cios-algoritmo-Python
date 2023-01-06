salario = float(input('Digite o valor do salário atual: R$'))
print(f'salário antes do reajuste era de R${salario}')

if salario <= 280:
  aumento = salario * 0.20
  print(f'O valor do aumento é R${aumento}')
  novo_salario = salario + aumento
  print(f'Salário com reajuste R${novo_salario}')
elif salario <= 700:
  aumento = salario * 0.15
  print(f'O valor do aumento é R${aumento}')
  novo_salario = aumento + salario
  print(f'Salário com reajuste R${novo_salario}')
elif salario <= 1500:
  aumento = salario * 0.15
  print(f'O valor do aumento é R${aumento}')
  novo_salario = aumento + salario
  print(f'Salário com reajuste R${novo_salario}')
elif salario >= 1500:
  aumento = salario * 0.10
  print(f'O valor do aumento é R${aumento}')
  novo_salario = salario + aumento
  print(f'Salário com reajuste R${novo_salario}')