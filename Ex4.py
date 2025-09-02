def tabuada(num):
    print(f"Tabuada do {num}: ")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

continua = "s"

while continua == "s" or continua == "S":
    num = int(input("Escolha um número: "))
    tabuada(num)
    continua = input("Deseja continuar? (s/n) ")
    if continua != "s" and continua != "S":
        print("Encerrando o programa...")
    