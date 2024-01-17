idade_usuario = int(input('Digite sua idade: '))

if idade_usuario <= 12:
    print('Categoria: Criança')
elif idade_usuario > 12 and idade_usuario <=18:
    print('Categoria: Adolescente')
elif idade_usuario > 18:
    print('Categoria: Adulto')

