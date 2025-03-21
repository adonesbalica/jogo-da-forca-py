from random import choice

import fileHandler as fh
import desenhos as d

def jogar():
    lista_palavras = list()
    arquivo = fh.abrir_arquivo_leitura('palavras.txt')

    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

    palavra_sorteada = choice(lista_palavras)

    for x in range(50):
        print()

    digitadas = []
    acertos = []
    erros = 0

    nome = input('Quem está jogando? ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        # CONDIÇÃO DE VITÓRIA
        if adivinha  == palavra_sorteada:
            print('Você acertou!')
            break

        # TENTATIVAS
        tentativa = input('\n   Digite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Você já usou essa letra!')
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print('Você errou!')

        score  = d.desenhar_forca(erros)

        # CONDIÇÃO DE FIM DE JOGO
        if erros == 6:
            print('Enforcado!')
            print(f'A palavra correte era: {palavra_sorteada}.')
            break

    fh.inserir_score('score.txt', nome, score)
