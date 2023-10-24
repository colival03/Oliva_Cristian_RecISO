ciudades= ["Merida","Badajoz","Caceres","Calamonte","Almendralejo","Zafra","Villanueva","Montijo","Villafranca","Plasencia","Azuaga"]
ciudad_usuario= input("Introduce el nombre de una ciudad: ")
ciudad_usuario = ciudad_usuario.lower()

if ciudad_usuario in [ciudad_usuario.lower for ciudad in ciudades]:
    print(f"{ciudad_usuario.capitalize()} se encuentra en el conjunto de ciudades.")
else:
    print(f"{ciudad_usuario.capitalize()} no se encuentra en el conjunto de ciudades")