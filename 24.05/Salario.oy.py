salario=float(input("Insira seu salário: "))
if salario > 8250:
    aumento=salario+(salario*0.1)
    porc=10
else:
    aumento=salario+(salario*0.15)
    porc=15
print("Seu salário era de R${}. Após um aumento de {}% ele é R${}.".format(salario,porc,aumento))