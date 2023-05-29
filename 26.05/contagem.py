def contagem_regressiva(a):
    while a > -1:
        print(a)
        a -= 1

n = int(input("Insira Um Número: "))
print(contagem_regressiva(n))