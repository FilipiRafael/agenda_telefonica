agenda = list()

def pede_nome():
    return input('Nome: ').lower()

def pede_telefone():
    return input('Telefone: ')

def pede_email():
    return input("Email: ")

def mostra_dados(nome, telefone, email):
    print(f'Nome: {nome} Telefone: {telefone} Email: {email}')

def pede_nome_arquivo():
    return input('Nome do arquivo: ')

def pesquisa(nome):
    global agenda
    mnome = nome.lower()
    for contador, pessoa in enumerate(agenda):
        if pessoa[0].lower() == mnome:
            return contador
    return None

def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    email = pede_email()
    agenda.append([nome, telefone, email])

def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        confirma = str(input('Deseja mesmo continuar esta alteração? [S/N]: ')).lower()
        if confirma in "Nn":
            print('Cancelando!')
            exit
        else:
            del agenda[p]
    else:
        print('Nome não encontrado!')

def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        email = agenda[p][2]
        print('Encontrado:')
        mostra_dados(nome, telefone, email)
        nome = pede_nome()
        telefone = pede_telefone()
        email = pede_email()
        confirma = str(input('Deseja mesmo continuar esta alteração? [S/N]: ')).lower()
        if confirma in "Nn":
            print('Cancelando!')
            exit
        else:
            agenda[p] = [nome, telefone]
    else:
        print("Nome não encontrado!")
    
def lista():
    if len(agenda) >= 1:
        print('\nAgenda\n\n--------')
        contador = 1
        for pessoa in agenda:
            print(contador, '- ', end='') 
            mostra_dados(pessoa[0], pessoa[1], pessoa[2])
            contador += 1
        print('--------\n')
    else:
        print(f'Não há nenhuma pessoa cadastrada na agenda.')

def read():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            agenda = list()
            for l in arquivo.readlines():
                nome, telefone, email = l.strip().split("#")
                agenda.append([nome, telefone, email])
            print(agenda)
    except FileNotFoundError:
        print('Arquivo não encontrado!')

def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}#{e[2]}\n")

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}!")

def mostrar_tamanho():
    global agenda
    arquivo = pede_nome_arquivo()
    try:
        with open(arquivo, 'r', encoding='utf-8') as arquivo:
            contador = 1
            for linha in arquivo.readlines():
                contador += 1
        if contador == 1:
            return print('Apenas uma pessoa cadastrada na agenda.')
        else:
            return print(f'Há {contador} pessoas cadastradas na agenda.')
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        
def ordenar_agenda():
    # Função em desenvolvimento
    nome_arquivo = pede_nome_arquivo()
    nomes = list()
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo.readlines():
                nome = linha.strip().split('#')
                nomes.append([nome[0]])
            return print(nomes.sort())
    except FileNotFoundError:
        print('Arquivo não encontrado!')

def menu():
    print("""
    1 - Novo
    2 - Alterar
    3 - Apagar
    4 - Listar
    5 - Gravar
    6 - Ler
    7 - Tamanho da agenda
    8 - Ordenar agenda
    0 - Sair do programa
    """)
    return valida_faixa_inteiro("Escolha uma das opções: ", 0, 8)

