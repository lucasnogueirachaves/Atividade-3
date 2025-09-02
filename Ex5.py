def somatorio(num):
    somatorio = 0
    for i in range(1, num + 1):
        somatorio += i
    return somatorio 

n = int(input("Digite um número: "))
print(f"O somatório é {somatorio(n)}")
    
