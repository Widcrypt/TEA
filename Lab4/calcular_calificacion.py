nota = float(input("Ingresa nota obtenida: "))

calificacion = ('Sobresaliente', 'Notable', 'Bien', 'Suficiente', 'Insuficiente')

if 0.9< nota <= 1.0:
   print(calificacion[0])
elif  0.8 < nota <= 0.9:
   print(calificacion[1])
elif 0.7 < nota <= 0.8:
   print(calificacion[2])
elif 0.6 < nota <= 0.7:
   print(calificacion[3])
elif nota <= 0.6:
   print(calificacion[4])
else:
   nota< 0.0 or nota>1.0
   print("Favor ingresar numéro entre 0.0 y 1.0")  