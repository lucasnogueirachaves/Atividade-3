'''
O programa deve permitir adicionar novas novelas,
consultar audiências, filtrar sucessos (audiência > 40 pontos), e calcular
estatísticas como média de audiência e ranking das novelas.

'''

novelas = {"violeta": 30, "eu sou franky": 10, "regra do jogo": 40, "avenida brasil": 50}

def adicionar(novelas):
    novela = input("Digite uma novela: ")
    audiencia = input("Digite a audiência: ")
    if novela not in novelas.keys():
        novelas.update({novela: int(audiencia)})
    else:
        print("Essa novela já está no dicionário! ")

def consulta(novelas):
    novela = input("Qual novela deseja descobrir a audiência? ")
    if novela in novelas.keys():
        print(novelas[novela])
    else:
        adicionar = input("Essa novela não está no dicionário, deseja adicionar? (s/n) ")
        if adicionar == "s" or adicionar == "S":
            audiencia = int(input("Digite a audiencia dessa novela: "))
            novelas.update({novela: audiencia})

def sucessos(novelas):
    lista_sucessos = [novela for novela in novelas.keys() if novelas[novela] > 40 ]
    print(f"\n Lista de sucessos: {lista_sucessos}")

def media(novelas):
   media = sum(novelas.values()) / len(novelas.values())
   print(f"A média é: {media}")

def ranking(novelas):
    ranking = dict(sorted(novelas.items(), key=lambda item: item[1], reverse=True))
    for i, novela in enumerate(ranking, start=1):
        print(f"{i}: {novela} -> {ranking[novela]}")

while True:
    print("\nEscolha uma opção: ")
    print("1. Adicionar novela")
    print("2. Consultar novela")
    print("3. Consultar sucessos")
    print("4. Consultar média de audiência")
    print("5. Consultar ranking")
    print("0. Sair")

    opcao = input("Escolha uma opção: \n")

    if opcao == "1":
        adicionar(novelas)
    elif opcao == "2":
        consulta(novelas)
    elif opcao == "3":
        sucessos(novelas)
    elif opcao == "4":
        media(novelas)
    elif opcao == "5":
        ranking(novelas)
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida, tente novamente.")