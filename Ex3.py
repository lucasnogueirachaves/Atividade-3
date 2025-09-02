def media(*args):
    soma = 0
    valido = True
    for nota in args:
        if 0 > nota > 10:
            print("Nota inválida")
            valido = False
            break
        else:
            soma += nota
    if valido:
        media = soma / len(args)
        if media < 5:
            print("Reprovado!")
        elif 7 > media >= 5:
            print("Recuperação!")
        else:
            print("Aprovado!")
        print(media)

media(10, 10)      
    