def tabla_multiplicar():
    i = 1
    j = 1
    while i != 0:
        i = int(input("Escribe un número. Pulsa 0 para finalizar: "))
        if i != 0:
            j = 1
            while j < 11:
                r = i * j
                print(f"{i} x {j} = {r}")
                j += 1

tabla_multiplicar()
