nota = float(input("Digite a nota do competidor: "))

if nota > 90:
    premio = "Medalha De Ouro"
elif nota <= 90 and nota >70:
    premio = "Medalha De Prata"
elif nota >= 70:
    premio = "Medalha De Bronze"
elif nota >= 60:
    premio = "Certificado De Menção Honrosa"
else: 
    premio = "Certificado De Participação"

print(f"O competidor ganhou o prêmio de {premio}.")
