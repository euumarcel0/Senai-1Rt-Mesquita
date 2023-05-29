def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
n = int(input("Insira Um Número: "))
par = verificar_par(n)
print("Seu Numero é",n,":",par)
