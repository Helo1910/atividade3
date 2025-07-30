Filmes = []

def cadastrar_filmes():
    nome = str(input('Entre com o nome da filmes ou série: '))
    plataforma = str(input('Qual a plataforma que será usada: '))
    genero = str(input('Qual o gênero: '))
    atualizacao_status = str(input('Já foi assistido ou está assistindo ou não foi assistido:'))
    Filme = {'nome':nome,
              'plataforma':plataforma,
              'genero':genero,
              'atualização':atualizacao_status}
    Filmes.append(Filme)
    print("😁😁Filme ou Série cadastrada com Sucesso!!!😁😁")
cadastrar_filmes()



def exibir_menu():
    while True:
        print('=== Sistema de Filmes e Séries ===')
        print('1- Cadastrar novo Filme ou Série✍✍✍')
        print('2- Ver todos os Filmes e Séries😎🎇')
        print('3- Buscar por gêneros e plataforma✨✨')
        print('4- Sair🤗🤗')

        escolha = str(input('Escolha uma opção: '))
        if escolha == '1':
            cadastrar_filmes()
        elif escolha =='2':
            buscar_filmes()
        elif escolha == '3':
            ver_cadastrados()
        elif escolha == '4':
            print(' Saindo do Sistema. Até a próxima')
            break
        else:
            print('Opção Inválida. Tente novamente. \n')
exibir_menu()
