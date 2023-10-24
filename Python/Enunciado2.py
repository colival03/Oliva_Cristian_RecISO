numero = input("Introduce un número: ")

if numero == numero[::-1]: #Esto te invierte el número como cadena.
    print(f"{numero} es un número capicúa.")
else:
    print(f"{numero} no es un número capicúa.")
