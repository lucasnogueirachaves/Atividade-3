def primo(n1, n2):
    lista_primos = []
    for i in range(n1, n2 + 1):
        if i == 1 or i == 0:
            primo = False
            continue
        else:
            primo = True
        for j in range(2, i - 1):
            if i % j == 0:
                primo = False
                break
        if primo:
            lista_primos.append(i)
            
    return lista_primos
        
            
print(*primo(0, 100))            