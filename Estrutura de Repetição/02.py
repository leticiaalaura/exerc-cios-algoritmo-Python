nome = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')

while nome == senha:
  print('ERRO: O usuário não pode ser igual a senha, tente novamente!')
  nome = input('Digite o nome de usuário: ')
  senha = input('Digite a senha: ')
else:
  print('Cadastro efetuado com sucesso!')
