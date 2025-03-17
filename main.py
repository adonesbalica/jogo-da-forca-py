import jogo as j
import fileHandler as fh

def mostrar_menu():
    print('=' *30)
    print(" " * 7 + "JOGO DA FORCA")
    print('=' *30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR\n")
    print("=" * 30)

arquivo = 'score.txt'
if fh.existe_arquivo(arquivo):
    print('Arquivo foi localizado no computador.')
else:
    print('Arquivo não existe.')
    fh.criar_arquivo(arquivo)

while True:
    mostrar_menu()
    opcao = int(input('Escolha a opção (1/2/3): '))

    match(opcao):
        case 1:
            print('Iniciar jogo')
            j.jogar()
        case 2:
            print('SCORE')
            dados = fh.listar_arquivo('score.txt')
            if not dados:
                print('Score vazio.')
            else:
                i = 1
                for jogador in dados:
                    print(f'{i} -> {jogador[0]}, Pontução: {jogador[1][:1]}')
                    i += 1
        case 3:
            print('Saindo do jogo, Atá mais!')
            break
        case _:
            print('Opção inválida. Tente outra.')
