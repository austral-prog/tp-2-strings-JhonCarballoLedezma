def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    
    gasto = float(input("ingrese el gasto: "))
    dinero_recibido=int(input("ingrese el dinero recibido: "))

    print("Ingresar gasto:") #67.4
    print(gasto)
    print("Dinero recibido")#200
    print(dinero_recibido)
    print("")
    print("Vuelto") #132.6
    print("")
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    print("Pesos:")
    print(pesos)
    centavos = round((vuelto - pesos) * 100 )
    print("Centavos:")
    print(centavos)

#change()
