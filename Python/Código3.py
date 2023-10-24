def un_proceso():
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

un_proceso()

'''Realiza un proceso en el que te muestre la tabla de multiplicar 
   y para finalizar pulsar la tecla 0.'''