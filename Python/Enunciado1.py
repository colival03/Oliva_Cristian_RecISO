calificaciones=[]

for i in range(5):
    calificacion = float(input(f"Ingrese la calificación del módulo {i + 1}: "))
    calificaciones.append(calificacion)

calificacion_maxima = max(calificaciones)
calificacion_minima = min(calificaciones)
media = sum(calificaciones) / len(calificaciones)

print(f"Calificación mayor: {calificacion_maxima}")
print(f"Calificacion menor: {calificacion_minima}")
print(f"Nota media de las calificaciones: {media}")
