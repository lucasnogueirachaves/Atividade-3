def soma(*args):
    historico.append(("soma", args, sum(args)))
    return sum(args)
    
def subtracao(*args):
    sub = args[0]
    for num in range(1, len(args)):
        sub -= args[num]
    historico.append(("subtracao", args, sub))
    return sub

def multiplicacao(*args):
    multi = args[0]
    for num in range(1, len(args)):
        multi *= args[num]
    historico.append(("multiplicacao", args, multi))
    return multi

def divisao(*args):
    div = args[0]
    for num in range(1, len(args)):
        div /= args[num]
    historico.append(("divisao", args, div))
    return div

historico = []

while True:
    try:
        print("\nQual operação deseja realizar? ")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Ver histórico")
        print("0. Fechar calculadora")

        opcao = input("Escolha uma opção: \n")

        if opcao == "1":
            print(f"O resultado é -> {soma(*map(int, input('Digite os números para realizar a operação: ').split()))}")
        elif opcao == "2":
            print(f"O resultado é -> {subtracao(*map(int, input('Digite os números para realizar a operação: ').split()))}")
        elif opcao == "3":
            print(f"O resultado é -> {multiplicacao(*map(int, input('Digite os números para realizar a operação: ').split()))}")
        elif opcao == "4":
            print(f"O resultado é -> {divisao(*map(int, input('Digite os números para realizar a operação: ').split()))}")
        elif opcao == "5":
            for i in range(len(historico)):
                print(f"Operação {i + 1} de {historico[i][0]} -> {historico[i][1]} = {historico[i][2]}")
        elif opcao == "0":
            print("Encerrando o programa...")
            historico = []
            break
    except ValueError:
        print("Entrada inválida")
    
        
        

