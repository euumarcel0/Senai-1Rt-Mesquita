def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def maior_numero(a, b):
    return max(a, b)

def menor_numero(a, b):
    return min(a, b)

def main():
    a = float(input("\nDigite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))

    print("\nSelecione uma opção:")
    print("a. Somar")
    print("b. Multiplicar")
    print("c. Maior número")
    print("d. Menor número")

    opcao = input("Opção: ")

    if opcao == 'a':
        resultado = somar(a, b)
    elif opcao == 'b':
        resultado = multiplicar(a, b)
    elif opcao == 'c':
        resultado = maior_numero(a, b)
    elif opcao == 'd':
        resultado = menor_numero(a, b)
    else:
        print("Opção inválida!")
        return

    print("\nResultado:", resultado)

main()
