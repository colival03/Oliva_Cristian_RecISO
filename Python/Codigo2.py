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
                print(str(a) + 'seleccionado') 
            else: 
                print(str(a) + 'no seleccionado') 
            print(r) 
    print("ya terminamos")
    
un_proceso()

'''Este código actua de la siguiente manera al iniciarlo lo primero que hará es preguntarle al usuario
   si desea ejecutar el programa, si el usuario introduce la letra n se terminará el programa y mostrará ya terminamos, porque no entra en el bucle if.
   
   Pero si el usuario introduce la letra s entra el el bucle if en el que la variable c está igualada a 0, para después entrar en un bucle while en el se ejecuta
   solo si c es menor, con la variable a le pide al usuario números y luego se almacena el resultado en la variable c que va incrementando +1 por cada vez que el 
   usuario introduzca un número y cuando c sea mayor de 10 sale del bucle e imprime ya terminamos'''