def existe_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def abrir_arquivo_leitura(nome_arquivo):
    try:
        a = open(nome_arquivo, 'r')
    except:
        print("Não foi possível abrir para leitura.")
    else:
        print(f'Arquivo {nome_arquivo} aberto com sucesso.')
        return a

def criar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso!\n')

def listar_arquivo(nome_arquivo):
    dados = []  # Inicializar dados para evitar erros
    try:
        a = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        dados = a.readlines()
    finally:
        a.close()
        return dados

def inserir_score(nome_arquivo, nome_jogador, score):
    try:
        a = open(nome_arquivo, 'a')  # Usar 'a' para adicionar ao arquivo
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write('{}:{}\n'.format(nome_jogador, score))
    finally:
        a.close()
