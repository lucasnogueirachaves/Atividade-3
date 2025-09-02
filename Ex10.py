lista_produtos = [{
    "nome": "camiseta do flamengo",
    "categoria": "roupas",
    "preco": 89.90,
    "estoque": 15,
    "origem": "rio de janeiro"
}, 
    {
    "nome": "camiseta do fluminense",
    "categoria": "roupas",
    "preco": 99.90,
    "estoque": 10,
    "origem": "rio de janeiro"
}, 
    {
    "nome": "camiseta do vasco",
    "categoria": "roupas",
    "preco": 79.90,
    "estoque": 4,
    "origem": "rio de janeiro"        
},
    {
    "nome": "hamburguer",
    "categoria": "comida",
    "preco": 15.00,
    "estoque": 50,
    "origem": "marica"
}]

def busca_pelo_nome(lista_produtos, vendas, valor):
    nome = input("Qual produto deseja buscar? ")
    tem = False
    vendas = 0
    valor = 0
    for i in range(len(lista_produtos)):
        if lista_produtos[i]["nome"] == nome:
            tem = True
            print(f"Produto -> nome: {lista_produtos[i]["nome"]}, categoria: {lista_produtos[i]["categoria"]}, preço: {lista_produtos[i]["preco"]}, estoque: {lista_produtos[i]["estoque"]}, origem: {lista_produtos[i]["origem"]}")
            if input(("Deseja comprar? (s/n) ")) == "s":
                lista_produtos[i]["estoque"] -= 1
                vendas += 1
                valor += lista_produtos[i]["preco"]
                print(f"Você comprou {lista_produtos[i]["nome"]}")
    if not tem:
        print("Não está na lista!")
    return vendas, valor

def adicionar(lista_produtos):
    nome = input("Qual o nome do produto a ser adicionado? ")
    categoria = input("Qual a categoria do produto? ")
    preco = float(input("Qual o preço? "))
    estoque = int(input("Quanto em estoque? "))
    origem = input("Qual a origem? ")
    lista_produtos.append({"nome": nome,
    "categoria": categoria,
    "preco": preco,
    "estoque": estoque,
    "origem": origem})
    
def produtos_disponiveis(lista_produtos):
    lista = []
    for i in range(len(lista_produtos)):
        if lista_produtos[i]["estoque"] > 0:
            lista.append(lista_produtos[i]["nome"])
    print(f"Os produtos disponíveis são: {", ".join(lista)}")


def listar_produtos_por_categoria(lista_produtos):
    lista = []
    categoria = input("Qual categoria? ")
    for i in range(len(lista_produtos)):
        if lista_produtos[i]["categoria"] == categoria.lower():
            lista.append(lista_produtos[i]["nome"])
    print(f"Os produtos que pertencem a essa categoria são: {", ".join(lista)}")

def quantidade(lista_produtos):
    quantidade = 0
    for i in range(len(lista_produtos)):
        quantidade += lista_produtos[i]["estoque"]
    print(f"A quantidade de produtos é: {len(lista_produtos)} e a quantidade total é: {quantidade}")
    
vendas = 0
valor = 0

while True:
    print("\nQual operação deseja realizar? ")
    print("1. Buscar produto pelo nome")
    print("2. Adicionar produto")
    print("3. Consultar produtos disponíveis")
    print("4. Listar produtos por categoria")
    print("5. Consultar quantidade de produtos")
    print("6. Consultar quantidade de vendas")
    print("0. Encerrar o programa")

    opcao = input("Escolha uma opção: \n")

    if opcao == "1":
        a, b = busca_pelo_nome(lista_produtos, vendas, valor)
        vendas += a
        valor += b
    elif opcao == "2":
        adicionar(lista_produtos)
    elif opcao == "3":
        produtos_disponiveis(lista_produtos)
    elif opcao == "4":
        listar_produtos_por_categoria(lista_produtos)
    elif opcao == "5":
        quantidade(lista_produtos)
    elif opcao == "6":
        print(f"A quantidade de vendas foi: {vendas} e o valor total foi: {valor:.2f}")
    elif opcao == "0":
        print("Encerrando o programa...")
        break