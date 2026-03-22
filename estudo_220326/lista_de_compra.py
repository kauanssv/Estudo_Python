lista = []
continuar = False
while(continuar == False):
    lista.append(input("Escreva algo para colocar na lista\n"))
    continua = str(input("Voce deseja colocar algo na lista? Sim ou Nao?\n"))
    if(continua == "Sim" or continua == "sim"):
        continuar = False
    elif(continua == "Nao" or continua == "nao"):
        for lista in lista:
            print(lista)
        break