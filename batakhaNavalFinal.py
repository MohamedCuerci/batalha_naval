# -*- coding: UTF-8 -*-
import random
import os
import time

def criar_tabuleiro(tamanho):
    tabuleiro = []
    posicoes_tabuleiro = list(range(tamanho))
    for linha in posicoes_tabuleiro:
        linha_matriz = []
        # contruir uma linha com a quantidade de colunas equivalentes ao tamanho da matriz
        for coluna in range(tamanho):
            linha_matriz.append(".")
        tabuleiro.append(linha_matriz)

    return tabuleiro

def inserir_valor(tabuleiro, linha, coluna, caractere):
    tabuleiro[linha-1][coluna-1] = caractere

    return tabuleiro

def existe_posicao_jogada(tamanho, linha, coluna):
    posicoes = list(range(tamanho))
    if linha - 1 not in posicoes or coluna -1 not in posicoes:
        return False
    else:
        return True

def retorna_conteudo_posicao(tabuleiro, linha, coluna):
    linha -= 1
    coluna -= 1
    return tabuleiro[linha][coluna]

def posicao_esta_livre(tabuleiro, linha, coluna):
    if retorna_conteudo_posicao(tabuleiro, linha, coluna) == ".":
        return True
    else:
        return False

def obter_linha_coluna():
    entrada_ok = False
    while not (entrada_ok):
        # garante que tenhamos apenas dois valores inteiros digitados
        try:
            linha, coluna = map(int,input("Digite dois valores separados por espaco, LINHA COLUNA: ").strip(" ").split(" "))
            entrada_ok = True
        except ValueError:
            print("[ERRO] Informe apenas dois valores númericos separados por espaço.")

    return linha, coluna

def obter_posicao_computador(tabuleiro, inicializando_tabuleiro = True):
    entrada_ok = False
    tamanho = len(tabuleiro)

    while not entrada_ok:
        linha = random.randint(1,tamanho)
        coluna = random.randint(1,tamanho)

        caractere = retorna_conteudo_posicao(tabuleiro, linha, coluna)
        if posicao_esta_livre(tabuleiro, linha, coluna) and inicializando_tabuleiro:
            entrada_ok = True
        elif not inicializando_tabuleiro:
            if caractere not in ("X","."):
                entrada_ok = False
            else:
                entrada_ok = True
    return linha, coluna

def obter_posicao_usuario(tabuleiro, inicializando_tabuleiro = True):
    validacoes_ok = False
    while not validacoes_ok:
        linha, coluna = obter_linha_coluna()

        if not existe_posicao_jogada(len(tabuleiro), linha, coluna):
            print("[ERRO] Informe uma posição que exista no tabuleiro")
        else:
            caractere = retorna_conteudo_posicao(tabuleiro,linha,coluna)
            if not posicao_esta_livre(tabuleiro, linha, coluna) and inicializando_tabuleiro:
                print("[ERRO] Esta posição já foi jogada anteriormente")
            #nao pode jogar em posicoes que sejam * ou # pois já foram jogadas
            elif not inicializando_tabuleiro and caractere not in ("X","."):
                print("[ERRO] Esta posição já foi jogada anteriormente")
            else:
                validacoes_ok = True

    return linha, coluna

def imprime_borda_superior_inferior(tamanho_matriz):
    # define a quantidade de tracos a serem impressos para formar a linha superior e inferior da tabela
    print("    ", end="")
    qtde_tracos = (tamanho_matriz * 2)
    sequencia_tracos = "  +" + qtde_tracos * "-" + "-+"
    print(sequencia_tracos, end="")
    print("              ", end="")
    print(sequencia_tracos)

def imprime_numeros_colunas():
    # variavel que utilizaremos para concatenar os numeros que identificam visualmente as colunas
    sequencia_numeros = "    "
    # produz a sequencia de numeros equivalentes a quantidade de colunas
    for i in range(len(tabuleiro_usuario)):
        sequencia_numeros += str(i + 1) + " "
    print("    ", end="")
    print(sequencia_numeros, end="")
    print("               ", end="")
    print(sequencia_numeros)

def imprime_tabuleiro(tabuleiro_usuario, tabuleiro_computador):
    os.system('cls')
    tamanho_matriz = len(tabuleiro_usuario)

    print("    ", end="")
    print("Tabuleiro do Usuário", end="")
    print("              ", end="")
    print("Tabuleiro do Computador")
    print()

    # imprime os numeros que identificam as colunas das tabelas
    imprime_numeros_colunas()

    # imprime a linha superior das tabelas
    imprime_borda_superior_inferior(tamanho_matriz)

    posicoes_da_matriz = range(1,tamanho_matriz+1)

    # imprime os valores das matrizes linha por linha
    for linha in (posicoes_da_matriz):
        print("    ", end="")
        # forma o numero da linha e a parede esquerda da primeira tabela
        print(str(linha) + " | ", end="")

        # imprime o conteudo da primeira matriz

        for coluna in posicoes_da_matriz:
            conteudo = retorna_conteudo_posicao(tabuleiro_usuario, linha, coluna)
            print(conteudo + " ", end="")
        # imprime a parede direita da primeira tabela
        print("|", end="")
        # imprime a quantidade de espacos entre as duas tabelas
        print("              ", end="")
        # imprime o numero da linha e a parede esquerda da segunda tabela
        print(str(linha) + " | ", end="")

        # imprime o conteudo da segunda matriz
        for coluna in posicoes_da_matriz:
            caractere = retorna_conteudo_posicao(tabuleiro_computador, linha, coluna)
            if caractere == "X":
                print("." + " ", end="")
            else:
                print(caractere + " ", end="")
        # imprime a parede da direita da segunda tabela
        print("|")
    # imprime a linha inferior das tabelas
    imprime_borda_superior_inferior(tamanho_matriz)

def inicializar_tabuleiro_usuario(tabuleiro_usuario,tabuleiro_computador, qtde_barcos):
    imprime_tabuleiro(tabuleiro_usuario, tabuleiro_computador)
    print(f"\nVocê marcará agora {qtde_barcos} barcos para iniciarmos o jogo!")
    for barco in range(qtde_barcos):
        linha, coluna = obter_posicao_usuario(tabuleiro_usuario)
        tabuleiro_usuario = inserir_valor(tabuleiro_usuario,linha,coluna,"X")
        imprime_tabuleiro(tabuleiro_usuario,tabuleiro_computador)

    return tabuleiro_usuario

def inicializar_tabuleiro_computador(tabuleiro_computador, qtde_barcos):
    for qtde_posicoes in range(qtde_barcos):
        linha, coluna = obter_posicao_computador(tabuleiro_computador)
        tabuleiro_computador = inserir_valor(tabuleiro_computador,linha,coluna,"X")

    return tabuleiro_computador

def marcar_posicao_atingida(tabuleiro,linha,coluna):
    caractere = retorna_conteudo_posicao(tabuleiro, linha, coluna)
    atingiu_algum_alvo = False
    if caractere == ".":
        tabuleiro = inserir_valor(tabuleiro,linha,coluna,"*")
    elif caractere == "X":
        tabuleiro = inserir_valor(tabuleiro, linha, coluna, "#")
        atingiu_algum_alvo = True

    return tabuleiro, atingiu_algum_alvo

#tamanho do tabuleiro
tamanho = 4
#quantidade de barcos
qtde_barcos = 5

acertos_usuario = 0
acertos_computador = 0

tabuleiro_usuario = criar_tabuleiro(tamanho)
tabuleiro_computador = criar_tabuleiro(tamanho)
tabuleiro_usuario = inicializar_tabuleiro_usuario(tabuleiro_usuario,tabuleiro_computador,qtde_barcos)
tabuleiro_computador = inicializar_tabuleiro_computador(tabuleiro_computador,qtde_barcos)

print("\n=============================== Regras do Jogo ==============================")
print("\nQuem acerta um barco do oponente repete a jogada.")
print("O X representa o posicionamento dos barcos.")
print("O * representa um tiro na água.")
print("O # representa um tiro que acertou o barco do oponente.")
print("\nJogo Iniciado.")

#True e o usuario
#Fase e o computador
vez_do_usuario = True
teve_ganhador = False

while not teve_ganhador:
    if vez_do_usuario:
        linha, coluna = obter_posicao_usuario(tabuleiro_computador,False)
        tabuleiro_computador, acertou_alvo = marcar_posicao_atingida(tabuleiro_computador,linha,coluna)
        if not acertou_alvo:
            #alterna pra vez do computador
            vez_do_usuario = False
        else:
            acertos_usuario += 1
            vez_do_usuario = True

    #vez do computador
    else:
        linha, coluna = obter_posicao_computador(tabuleiro_usuario, False)
        tabuleiro_usuario, acertou_alvo = marcar_posicao_atingida(tabuleiro_usuario,linha,coluna)
        if not acertou_alvo:
            #alterna pra vez do usuario
            vez_do_usuario = True
        else:
            acertos_computador += 1

        print(f"\nO computador jogou na posicao linha: {linha} coluna: {coluna}\n")
        time.sleep(2)

    imprime_tabuleiro(tabuleiro_usuario,tabuleiro_computador)

    if acertos_usuario == qtde_barcos or acertos_computador == qtde_barcos:
        teve_ganhador = True

if acertos_usuario == 5:
    print("Parabéns ao usuário que venceu a partida. ")
else:
    print("Parabéns ao computador que venceu a partida. ")
















""" notap1 = float(input('p1: '))
            if notap1 > 0 and notap1 <= 10:
                lista.append(notap1)
            elif notap1 == '':
                lista.append(' ')
            notap2 = float(input('p2: '))
            if notap2 > 0 and notap2 <= 10:
                lista.append(notap2)
            elif notap2 == '':
                lista.append(' ')
            notat1 = float(input('t1: '))
            if notat1 > 0 and notat1 <= 10:
                lista.append(notat1)
            elif notat1 == '':
                lista.append(' ')
            notat2 = float(input('t2: '))
            if notat2 > 0 and notat2 <= 10:
                lista.append(notat2)
            elif notat2 == '':
                lista.append(' ')
            break """