quadrados = [["", "", ""], ["", "", ""], ["", "", ""]]
nome_jogador1 = ""
nome_jogador2 = ""
escolha = ""
resultado = False

def carregarJogo():
    print(f'| {quadrados[0][0]} | {quadrados[0][1]} | {quadrados[0][2]} |')
    print(f'| {quadrados[1][0]} | {quadrados[1][1]} | {quadrados[1][2]} |')
    print(f'| {quadrados[2][0]} | {quadrados[2][1]} | {quadrados[2][2]} |')

def set_nome_jogador1():
  nome_jogador1 = input("Digite seu nome: ")

  return nome_jogador1

def set_nome_jogador2():
  nome_jogador2 = input("Digite seu nome: ")

  return nome_jogador2

def escolher():
  escolha = ""
  while escolha != "x" and escolha != "0" or escolha == "":
    escolha = input("Escolha X ou 0: ")
    return escolha

def jogadaDoJogador1(escolha, nome):
  jogada = ""
  linha = 3
  coluna = 3 
  while linha > 2 or coluna > 2:
    print(f"Vez de {nome}")
    linha = int(input("Escolha a linha: "))
    coluna = int(input("Escolha a coluna: "))

    while jogada != escolha or jogada == "":
      jogada = input("Jogue: ")
      print(escolha)


  quadrados[linha][coluna] = jogada

def jogadaDoJogador2(escolha, nome):
  jogada = ""
  linha = 3
  coluna = 3 

  while linha > 2 or coluna > 2:
    print(f"Vez de {nome}")
    linha = int(input("Escolha a linha: "))
    coluna = int(input("Escolha a coluna: "))

    while jogada == escolha or jogada != "x" and jogada != "0":
      jogada = input("Jogue: ")

  quadrados[linha][coluna] = jogada 

def verificar(jogador: str):
  resultado = False

  if quadrados[0][0] == quadrados[0][1] and quadrados[0][0] == quadrados[0][2] and quadrados[0][0] != "":
    print(f"Jogador {jogador} venceu")
    resultado = True
  elif quadrados[1][0] == quadrados[1][1] and quadrados[1][0] == quadrados[1][2] and quadrados[1][0] != "":
    print(f"Jogador {jogador} venceu")
    resultado = True
  elif quadrados[2][0] == quadrados[2][1] and quadrados[2][0] == quadrados[2][2] and quadrados[2][0] != "":
    print(f"Jogador {jogador} venceu")
    resultado = True
  elif quadrados[0][0] == quadrados[1][1] and quadrados[0][0] == quadrados[2][2] and quadrados[0][0] != "":
    print(f"Jogador {jogador} venceu")
    resultado = True
  elif quadrados[0][2] == quadrados[1][1] and quadrados[0][2] == quadrados[2][0] and quadrados[0][2] != "":
    print(f"Jogador {jogador} venceu")
    resultado = True

  return resultado  

nome_jogador1 = set_nome_jogador1()
escolha = escolher()

nome_jogador2 = set_nome_jogador2()

while resultado == False:
  carregarJogo()

  jogadaDoJogador1(escolha, nome_jogador1)
  resultado = verificar(nome_jogador1)

  if resultado == False:
    jogadaDoJogador2(escolha, nome_jogador2)
    resultado = verificar(nome_jogador2)
    if resultado == True:
      carregarJogo()
  else:
    carregarJogo()
