nota = float(input("Ingresa nota obtenida: "))

calificacion = ('Sobresaliente', 'Notable', 'Bien', 'Suficiente', 'Insuficiente')

if nota >= 0.9:
   print(calificacion[0])
elif nota >= 0.8:
   print(calificacion[1])
elif nota >= 0.7 :
   print(calificacion[2])
elif nota >= 0.6:
   print(calificacion[3])
elif nota <0.6:
   print(calificacion[4])
else:
   print("Puntaje fuera de rango")  