
def calificionNotas(notas):
    0.0 <= notas <= 1.0
    
    if notas< 0.9:
         print("Sobresaliente")
    elif 0.8<= notas < 0.9:
        print ("Notable")  
    elif 0.7< notas < 0.8: 
        print("Bien")
    elif notas <= 0.6: 
        print("Insuficiente") 
try: 
    notas = float(input ("Ingresa nota obtenida: "))
    print("Calificacion:", calificacion)

except:   
    print("Error, ingresar un numéro entre 0.0 y 1.0")  
