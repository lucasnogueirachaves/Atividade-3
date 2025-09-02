lista_tuplas = [("feijoada", "sudeste", 40), ("acarajé", "nordeste", 10), ("tacacá", "norte", 20), ("baião de dois", "nordeste", 25)]

def regiao(lista_tuplas):
    comidas = []
    reg = input("Qual região deseja consultar? ")
    for tupla in lista_tuplas: 
        if tupla[1] == reg.lower():
            comidas.append(tupla[0])
        
    if comidas:
        print(f"Comidas dessa região : {", ".join(comidas)}")
    else:
        print("Não há resultados")
    
def media_precos(lista_tuplas):
    soma = 0
    for tupla in lista_tuplas:
        soma += tupla[2]
    print(f"A média é {soma / len(lista_tuplas):.2f}")

def maior_preco(lista_tuplas):
    maior = 0
    for tupla in lista_tuplas:
        if tupla[2] > maior:
            maior = tupla[2]
            
    print(f"O maior preço é: {maior}")
    
while True:
    print("\nEscolha uma opção: ")
    print("1. Consultar região")
    print("2. Consultar média de preços")
    print("3. Consultar maior preço")
    print("0. Sair")

    opcao = input("Escolha uma opção: \n")

    if opcao == "1":
        regiao(lista_tuplas)
    elif opcao == "2":
        maior_preco(lista_tuplas)
    elif opcao == "3":
        maior_preco(lista_tuplas)
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida, tente novamente.")