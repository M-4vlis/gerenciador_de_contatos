import os, json, uuid

# Verifica se a pasta data existe, e caso ela não existe, cria a pasta e o arquivo contatos.json
if os.path.exists('./data'):
    file_contacts = './data/contatos.json'
else:
    os.mkdir('data')
    with open('data/contatos.json', 'w') as f:
        file_contacts = './data/contatos.json'

def carregar_contatos():
    if os.path.exists(file_contacts):
        try:
            with open(file_contacts, 'r') as f:
                lista_contatos = json.load(f)
                return lista_contatos
        except json.JSONDecodeError:
            print('Erro ao carregar arquivo, iniciando com lista de contatos vazia.')
            return []
    else:
        print('Arquivo não existe, iniciando com lista de contatos vazia.')
        return []

def cadastrar_contato(lista_contatos):
    while True:
        nome = str(input('Nome: '))

        while True:
            telefone = input('Telefone: ').strip().replace('-', '')
            if len(telefone) < 11 or not telefone.isdigit():
                print('Telefone inválido.')
                continue
            telefone = f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}'
            break

        while True:
            email = str(input('E-mail: '))
            if '@' in email and '.' in email:
                break
            print('E-mail inválido.')
        
        contato  = {
            'ID': str(uuid.uuid4()),
            'Nome': nome,
            'Telefone': telefone,
            'Email': email
        }
        lista_contatos.append(contato)
        print('\n✅ Contato cadastrado com sucesso.')
        salvar_contatos()
        opcao = str(input('\nDeseja cadastrar um novo contato? (S/N) ')).upper().strip()
        if opcao != 'S':
            break

def listar_contatos(lista_contatos):
    if not lista_contatos:
        print('Nenhum contato cadastrado.')
        return
    print('\n===== Lista de contatos =====:')
    for contato in lista_contatos:
        print('='*30)
        print('🔹 Contato')
        print("Nome:".ljust(10), contato['Nome'])
        print("Telefone:".ljust(10), contato['Telefone'])
        print("E-mail:".ljust(10), contato['Email'])
        print('='*30)

def salvar_contatos(lista_contatos):
    try:
        with open(file_contacts, 'w') as f:
            json.dump(lista_contatos, f, indent=4)
    except Exception as e:
        print(f'Erro inesperado: {e}')

def menu_principal(lista_contatos):
    while True:
        print('\n===== Menu ContatON =====')
        print('1 - Cadastrar novo contato\n' 
              '2 - Listar todos os contatos\n' 
              '3 - Sair\n')
        try:
            escolha = int(input('Escolha uma opção: '))
        except:
            print('Escolha inválida, digite um número.')
            continue
        if escolha == 1:
            cadastrar_contato(lista_contatos)
        elif escolha == 2:
            listar_contatos(lista_contatos)
        elif escolha == 3:
            print('Obrigado por usar o ContatON CLI. Até logo!')
            break
        else:
            print('Opção inválida.')
