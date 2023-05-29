quantidade = int(input("Quantos valores você quer usar para fazer a média? "))

valores = []
for i in range(quantidade):
    valor = float(input("Digite o valor {}: ".format(i+1)))
    valores.append(valor)

media = sum(valores) / quantidade
print("A média dos valores é: {:.2f}".format (media))