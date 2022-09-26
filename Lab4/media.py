contador = 0
suma = 0
promedio = 0 
primerNumero = True 
while True: 
    try:
        numero = input("Ingrese un numéro: ")
        if (numero == "salir"):
          break  
        else: 
            contador = contador + 1
            suma = suma + int(numero) 
            promedio = suma / contador  
    except:
        print("Error, debe ingresar un valor numérico")
        contador = contador - 1 
        continue
print("Contador:" , contador)
print("Sumatoria:" , suma)
print("Promedio:" , promedio)  
 