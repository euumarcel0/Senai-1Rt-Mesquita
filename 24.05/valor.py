velociade = int(input("Informe A Velocidade: "))

if velociade > 80: 
    valor =(velociade-80)*7
    print("Sua Velocidade Foi De:",velociade,"Km/h e", "Você Ultrapassou A Velociade Permitida De 80Km/h, Você está Multado ") 
    print("O Valor Da Sua Multa é De: R$",valor)
else:  
    print("Sua Velocidade Foi De:",velociade,"Km/h","Atenção Na Velocidade" )
