def par(n):
    if n % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
    
def linhas_alternadas(num_linhas):
    for i in range(num_linhas):
        if i % 2 == 0:
            print("Linha verde")
        else:
            print("Linha vermelha")
            
def cartao(num_cartao):
    if (num_cartao % 10) % 2 == 0:
        print("Cartão válido")
    else:
        print("Cartão inválido")       