def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: divisão por zero"

print("Selecione a operação:")
print("+ - Adição")
print("- - Subtração")
print("/ - Multiplicação")
print("* - Divisão")

escolha = input("Digite sua opção (+,-,/,*): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '+':
    print(num1, "+", num2, "=", adicao(num1, num2))
elif escolha == '-':
    print(num1, "-", num2, "=", subtracao(num1, num2))
elif escolha == '*':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
elif escolha == '/':
    print(num1, "/", num2, "=", divisao(num1, num2))
else:
    print("Opção inválida")
