a= 0
b= 0
c= 0
final= 1

while final != 0: 
    print("Escribir tres números distintos, por favor: ")
    a= float(input("Ingrese el primer número: "))
    b= float(input("Ingrese el segundo número: "))
    c= float(input("Ingrese el tercer número: "))
    
    if a>b:
        if a>c:
            print(" a mayor ", a) 
        else:   
            print(" c mayor ", c)
    else:
        if b>c:
            print(" b mayor ", b)
        else:
            print(" c mayor ", c) 

    print( "¿Quiere finalizar el proceso? Teclee 0 para salir.")
    final= int(input())

'''Realiza un programa en el que pida al usuario tres números distintos y de los tres que muestre el mayor de los tres y
   y para finalizar el programa presione la tecla 0.'''