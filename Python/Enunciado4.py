numero=int(input("Introduzca un número del 1 al 50: "))

if 1<= numero <=50:
    binario=bin(numero)
    octal=oct(numero)
    hexadecimal=hex(numero)
    print(f"Representación en binario: {binario}")
    print(f"Representación en octal: {octal}")
    print(f"Representación en hexadecimal: {hexadecimal}")
else:
    print(f"El número ingresado no se encuentra en el rango entre 1 y 50.")