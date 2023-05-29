import datetime

nome = input("Digite Seu Nome: ")
escolha = input("Digite '1' para exibir o mês por extenso ou '2' para exibir o mês numérico: ")

if escolha == '1':
    dia = int(input("Digite o Dia: "))
    mes = input("Digite o Mês Por Extenso: ")
    ano = int(input("Digite o Ano: "))
elif escolha == '2':
    dia = int(input("Digite o Dia: "))
    mes = int(input("Digite o Mês: "))
    ano = int(input("Digite o Ano: "))

if escolha == '1':
    print("Olá,", nome + ", sua data de nascimento é:", dia, "de", mes, "de", ano)
elif escolha == '2':
    print("Olá,", nome + ", você nasceu no dia", dia, "de", mes, "de", ano)

data_atual = datetime.datetime.now()
data_nascimento = datetime.datetime(ano, mes, dia)

diferenca = data_atual - data_nascimento

idade = diferenca.days // 365

print("Sua idade é:", idade, "anos.")
