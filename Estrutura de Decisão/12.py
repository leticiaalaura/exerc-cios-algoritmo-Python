valor_hora = float(input('Qual o valor da hora trabalhada? '))
horas_mes = int(input('Quantas horas mensais você trabalha? '))
salario_bruto = valor_hora * horas_mes
print(f'Salário Bruto: R${salario_bruto}')

if salario_bruto <= 900:
  print(f'Salário Bruto: R${salario_bruto}')
  sindicato = salario_bruto * 0.03
  print(f'(-) Sindicato: R${sindicato}')
  salario_liquido = salario_bruto - sindicato
  print(f'Isento de IR, o valor a receber é de R${salario_liquido}')
elif salario_bruto <= 1500:
  sindicato = salario_bruto * 0.03
  print(f'(-) Sindicato: R${sindicato}')
  ir = salario_bruto * 0.05
  print(f'(-) IR: R${ir}')
  total_desc = sindicato + ir
  print(f'Total de descontos: R${total_desc}')
  salario_liquido = salario_bruto - total_desc
  print(f'Salário Líquido: R${salario_liquido}')
elif salario_bruto <= 2500:
  sindicato = salario_bruto * 0.03
  print(f'(-) Sindicato: R${sindicato}')
  ir = salario_bruto * 0.10
  print(f'(-) IR: R${ir}')
  total_desc = sindicato + ir
  print(f'Total de descontos: R${total_desc}')
  salario_liquido = salario_bruto - total_desc
  print(f'Salário Líquido: R${salario_liquido}')
else:
  sindicato = salario_bruto * 0.03
  print(f'(-) Sindicato: R${sindicato}')
  ir = salario_bruto * 0.20
  print(f'(-) IR: R${ir}')
  total_desc = sindicato + ir
  print(f'Total de descontos: R${total_desc}')
  salario_liquido = salario_bruto - total_desc
  print(f'Salário Líquido: R${salario_liquido}')