nome_usuario = str(input('Usuário: '))
senha_usuario = int(input('Senha: '))
nome_padrao = 'banco'
senha_padrao = 123

if nome_usuario == nome_padrao and senha_usuario == senha_padrao:
    print('Acesso liberado')
else:
    print('Acesso negado')