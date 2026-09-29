# Programa que calcula o número de permutações, arranjos com e sem repetição e combinações

while True:
    k = int(input('Digite um valor para k: '))

    while k < 0:
        k = int(input('A variável k não pode ser negativa. Por favor, digite novamente: '))

    n = int(input('Digite um valor para n: '))

    while n < 0:
        n = int(input('A variável n não pode ser negativa. Por favor, digite novamente: '))

    while k < n:
        k = int(input(f'A variável k deve ser maior que a variável n. Por favor, digite um valor maior ou igual a {n}: '))

    x = 0

    permutacoesK = 1
    permutacoesN = 1
    permutacoesX = 1

    k_inicial = k
    n_inicial = n

    def permutacoes(k, n):
        k = k_inicial
        n = n_inicial

        permutacoesK = 1
        permutacoesN = 1
        permutacoesX = 1

        while k > 1:
            permutacoesK = permutacoesK * k
            k = k - 1
        
        if k < 1:
            permutacoesK = 1
        
        while n > 1:
            permutacoesN = permutacoesN * n
            n = n - 1
        
        if n < 1:
            permutacoesN = 1
        
        x = k_inicial - n_inicial

        while x > 1:
            permutacoesX = permutacoesX * x
            x = x - 1
        
        if x < 1:
            permutacoesX = 1
        
        return permutacoesK, permutacoesN, permutacoesX

    def arranjo_repetido(k, k_inicial, n):
        k = k_inicial
        n = n_inicial

        arr_repK = 0

        while n > 1:
            k = k_inicial * k
            arr_repK = k
            n = n - 1
        
        return arr_repK

    def arranjo(permutacoesK, permutacoesX):
        arr = permutacoesK // permutacoesX

        return arr

    def comb(permutacoesK, permutacoesN, permutacoesX):
        combs = permutacoesK // (permutacoesN * permutacoesX)

        return combs

    permutacoesK, permutacoesN, permutacoesX = permutacoes(k, n)

    arr_repK = arranjo_repetido(k, k_inicial, n)

    arr = arranjo(permutacoesK, permutacoesX)

    combs = comb(permutacoesK, permutacoesN, permutacoesX)

    print(f'\nNúmero de permutações do conjunto k: {permutacoesK}\n\n')

    print(f'Numero de arranjos com repetição formados com os elementos de k tomados {n} a {n}: {arr_repK}\n\n')

    print(f'Número de arranjos sem repetição formados com os elementos de k tomados {n} a {n}: {arr}\n\n')

    print(f'Número de combinações formadas com os elementos de k tomados {n} a {n}: {combs}\n\n')