while True:
    try:
        num = input('Digite um número: ')
        if int(num) <= 0:
            raise ValueError
        soma=0
        for i in num:
            soma += int(i)

        print(f"A soma dos algarismos é igual a {soma}")
        break
    except ValueError:
        print("Número inválido, tente novamente")