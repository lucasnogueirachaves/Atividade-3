lista_times = ["fluminense", "coritiba", "bahia", "mirassol", "flamengo", "vasco", "botafogo", "palmeiras", "altos", "portuguesa"]

def filtrar(times):
    letra_inicial = input("Digite a letra inicial: ")
    lista = [time for time in times if time[0] == letra_inicial.lower()]
    if lista:
        print(f"Times que começam com {letra_inicial}: {", ".join(lista)}")
    else:
        print("Não há resultados")
        
def adicionar(times):
    time = input("Digite um time para adicionar na lista: ")
    if time.lower() not in times:
        times.append(time)
    else:
        print("Esse time já está na lista!")

def remover(times):
    time = input("Qual time deseja remover? ")
    if time.lower() in times:
        times.remove(time)
    else:
        print("Esse time não está na lista!")
        
def busca(times):
    time = input("Qual time deseja buscar? ")
    if time.lower() in times:
        print(f"O time {time} está na lista!")
    else:
        print(f"O time {time} não está na lista!")
        
def mostrar_fatia(times):
    inicio = int(input("Digite o índice inicial: "))
    fim = int(input("Digite o índice final: "))
    print(f"{", ".join(times[inicio:fim])}")

while True:
    print("\nEscolha uma opção: ")
    print("1. Filtrar times pela primeira letra")
    print("2. adicionar time")
    print("3. Remover time")
    print("4. Buscar time")
    print("5. Mostrar fatia da lista")
    print("0. Sair")

    opcao = input("Escolha uma opção: \n")

    if opcao == "1":
        filtrar(lista_times)
    elif opcao == "2":
        adicionar(lista_times)
    elif opcao == "3":
        remover(lista_times)
    elif opcao == "4":
        busca(lista_times)
    elif opcao == "5":
        mostrar_fatia(lista_times)
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida, tente novamente.")