def cont_billetes(cantidad):
    billetes=[100,50,20,10,5]
    canti_billetes=[0,0,0,0,0]
    
    for i in range(5):
        canti_billetes[i] = cantidad // billetes[i]
        cantidad %= billetes[i]
    return canti_billetes

while True:
    cantidad=int(input("Introduzca una cantidad de dinero (hasta 3000 euros): "))
    if cantidad % 5 == 0 and cantidad <= 3000:
        billetes = cont_billetes(cantidad)
        cantidades=[100,50,20,10,5]
        
        for i in range(5):
            if billetes[i] > 0:
                print(f"Billetes de {cantidades[i]}:{billetes[i]}")
                break
    else:
        print(f"La cantidaad debe ser un múltilplo de 5 y no pasarse de 3000 euros.")
