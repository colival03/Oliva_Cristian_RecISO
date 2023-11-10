def un_proceso():
    a= 0
    r= 0
    c= 0
    pr= input("¿Desea ejecutar el programa? (s/n): ")
    
    if pr == "s":
        c = 0
        while c < 10:
            a = int(input("Ingrese un número: "))
            c += 1
            r = a % 2
            if r == 0:
                print(str(a) + ' seleccionado') 
            else: 
                print(str(a) + ' no seleccionado') 
            print(r) 
    print("ya terminamos")
    
un_proceso()
