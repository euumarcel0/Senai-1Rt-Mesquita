while True: 
    n = int(input("Insira O Número: "))

    if n < 0:
        break
    if n % 2 == 0:
        print("Seu Número é Par:")
    else:
        print("Seu Número é Impar:")
