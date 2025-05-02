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
            telefone_validado = validar_telefone(telefone)
            if telefone_validado == 'Telefone inválido.':
                continue
            break
        while True:
            email = str(input('E-mail: '))
            email_validado = validar_email(email)     
            if email_validado == 'E-mail inválido, digite novamente.':
                continue
            break
        
        contato  = {
            'ID': str(uuid.uuid4()),
            'Nome': nome,
            'Telefone': telefone_validado,
            'Email': email_validado
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
    print('5 - Editar contato')
    print('6 - Sair')

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
               4:excluir_contato,
               5:editar_contato}
    return funcoes

def menu_principal(lista_contatos):
    while True:
        escolha = obter_opcao_usuario()
        funcoes = obter_funcoes_menu()
        if escolha == 6:
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
                validar_email(termo_busca)

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
            salvar_contatos(lista_contatos)
            print('✅ Contato excluído com sucesso!')
            return True
        else:
            print('\nOK, exclusão de contato cancelada.')
            return False

def editar_contato(lista_contatos):
    spinner('Listando contatos', 10)
    listar_contatos(lista_contatos)
    while True:
        idContato = str(input('\nDigite o ID do contato que deseja alterar (ou Enter para voltar ao menu principal): ')).strip().lower()

        if not idContato:
            return
    
        contato = [(key, value) for key, value in enumerate(lista_contatos) if value['ID'].lower() == idContato]
        if len(contato) == 0:
            print('❌ Nenhum contato encontrado, tente novamente.')
            continue
        posicao = contato[0][0]
        value = contato[0][1]
        nome = value['Nome']
        telefone = value['Telefone']
        email = value['Email']

        print('\nContato encontrado:\n')
        print('🔹Contato')
        print('Nome:'.ljust(10), nome)
        print('Telefone:'.ljust(10), telefone)
        print('E-mail:'.ljust(10), email)

        novo_nome = str(input(f'\nNome atual: {nome} | Novo nome (ou Enter para manter): '))
        if novo_nome:
            value['Nome'] = novo_nome

        novo_telefone = str(input(f'Telefone atual: {telefone} | Novo telefone (ou Enter para manter): '))
        if validar_telefone(novo_telefone):
            value['Telefone'] = novo_telefone

        novo_email = str(input(f'E-mail atual: {email} | Novo e-mail (ou Enter para manter): '))
        if validar_email(novo_email):
            value['Email'] = novo_email

        lista_contatos[posicao] = value
        lista_contatos = sorted(lista_contatos, key=lambda x: x['Nome'])
        salvar_contatos(lista_contatos)
        print('\n✅ Contato alterado com sucesso.')
        return
    
def validar_email(email):
    while True:
        if not email:
            pergunta = input('E-mail em branco, deseja manter? (S/N)').strip().upper()
            if pergunta == 'S':
                return None
            else:
                continue
        if '@' in email and '.' in email:
            return email
        else:
            erro = 'E-mail inválido, digite novamente.'
            return erro
            

def validar_telefone(telefone):
    while True:
        if not telefone:
            pergunta = input('Telefone em branco, deseja manter? (S/N)').strip().upper()
            if pergunta == 'S':
                return None
            else:
                continue
        if len(telefone) < 11 or not telefone.isdigit():
            erro = 'Telefone inválido.'
            return erro
            
        telefone = f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}'
        return telefone

def spinner(texto, qtdVoltas):
    from time import sleep
    pins = ['|', '/', '-', '\\']

    for volta in range(qtdVoltas):
        for i in pins:
            print(texto, i, end='\r')
            sleep(0.1)
    