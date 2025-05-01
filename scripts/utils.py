import os, json, uuid

def obter_caminho_arquivo():
    if os.path.exists('./data'):
        caminho_arquivo = './data/contatos.json'
    else:
        os.mkdir('data')
        with open('data/contatos.json', 'w', encoding='utf-8') as f:
            caminho_arquivo = './data/contatos.json'
    return caminho_arquivo

FILE_CONTACTS = obter_caminho_arquivo()

def carregar_contatos():
    if os.path.exists(FILE_CONTACTS):
        try:
            with open(FILE_CONTACTS, 'r', encoding='utf-8') as f:
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
        lista_contatos = sorted(lista_contatos, key=lambda x: x['Nome'])
        salvar_contatos(lista_contatos)
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
        print("ID:".ljust(10), contato['ID'])
        print('='*30)

def salvar_contatos(lista_contatos):
    try:
        with open(FILE_CONTACTS, 'w', encoding='utf-8') as f:
            json.dump(lista_contatos, f, indent=4)
    except Exception as e:
        print(f'Erro inesperado: {e}')

def exibir_menu():
    print('\n===== Menu ContatON =====')
    print('1 - Cadastrar novo contato')
    print('2 - Listar todos os contatos')
    print('3 - Buscar contato')
    print('4 - Excluir contato')
    print('5 - Sair')

def obter_opcao_usuario():
    while True:
        exibir_menu()
        try:
            escolha = int(input('\nEscolha uma opção: '))
        except:
            print('Escolha inválida, digite um número.')
            continue
        return escolha
    
def obter_funcoes_menu():
    funcoes = {1:cadastrar_contato,
               2:listar_contatos,
               3:buscar_contatos,
               4:excluir_contato}
    return funcoes

def menu_principal(lista_contatos):
    while True:
        escolha = obter_opcao_usuario()
        funcoes = obter_funcoes_menu()
        if escolha == 5:
            print('Obrigado por usar o ContatON CLI. Até logo!')
            break
        if escolha in funcoes.keys():
            funcoes[escolha](lista_contatos)
        else:
            print('Opção inválida.')
            continue

def buscar_contatos(lista_contatos):
    while True:
        campo_escolhido = input('Buscar por (Nome/ E-mail): ').lower().strip().replace('-', '')
        opcoes_validas = ('nome', 'email')
        if campo_escolhido not in opcoes_validas:
            print('Opção inválida, tente novamente.')
            continue

        while True:
            termo_busca = input('Digite o termo de busca: ').lower().strip()
            if not termo_busca:
                print('Digite um termo válido.')
                continue
            if campo_escolhido == 'email':
                if '@' not in termo_busca and '.' not in termo_busca:
                        print('Digite um e-mail válido.')
                        continue
            resultado = [contato for contato in lista_contatos if termo_busca in contato[campo_escolhido.capitalize()].lower()]
            if len(resultado) == 0:
                print('\n❌ Nenhum contato encontrado.')
                return
            print('\nResultados encontrados:\n')
            for i in resultado:
                print('🔹 Contato')
                print(f'Nome: {i['Nome']}')
                print(f'Telefone: {i['Telefone']}')
                print(f'E-mail: {i['Email']}\n')
            return

def excluir_contato(lista_contatos):
    while True:
        id_contato = str(input('\nDigite o ID do contato que deseja excluir: '))
        if not id_contato:
            print('Digite um contato válido.\n')
            continue
        contato = None
        for key, value in enumerate(lista_contatos):
            if id_contato == value['ID']:
                posicao = key
                contato = value
                break
        if not contato:
            print('Contato não encontrado, tente novamente.')
            continue
            
        print('\nContato encontrado:\n')
        print('🔹Contato')
        print('Nome:'.ljust(10), contato['Nome'])
        print('Telefone:'.ljust(10), contato['Telefone'])
        print('E-mail:'.ljust(10), contato['Email'])
                    
        pergunta = str(input('\nDeseja realmente excluir? (S/N): ')).upper().strip()

        if pergunta == 'S':
            del lista_contatos[posicao]
            lista_contatos = sorted(lista_contatos, key=lambda x: x['Nome'])
            with open (FILE_CONTACTS, 'w', encoding='utf-8') as f:
                f = json.dump(lista_contatos, f, indent=4)
            print('✅ Contato excluído com sucesso!')
            return True
        else:
            print('\nOK, exclusão de contato cancelada.')
            return False