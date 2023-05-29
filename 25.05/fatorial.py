def fatorial(num):
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    return fatorial

num = int(input("Digite um número inteiro para calcular o fatorial: "))
resultado = fatorial(num)
print(f"O fatorial de {num} é {resultado}.")