while True:
    num = int(input("Digite um número (ou um valor negativo para sair): "))
    
    if num < 0:
        print("Programa encerrado.")
        break
    
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")
