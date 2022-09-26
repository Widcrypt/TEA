contador = 0
suma = 0
maximo = 0
minimo = 0 
primerNumero = True 
while True: 
    try:
        numero = input("Ingrese un numéro: ")
        if (numero == "salir"):
          break  
        else: 
            contador = contador + 1
            suma = suma + int(numero) 
        if (primerNumero):
               minimo = int(numero)
               maximo = int(numero)
               primerNumero = False
        else:
            if (int(numero) > maximo) : maximo = int(numero)
            if (int(numero) < minimo) : minimo = int(numero) 
    except:
        print("Error, debe ingresar un valor numérico")
        contador = contador - 1 
        continue 
print("Contador:" , contador)
print("Maximo:" , maximo)
print("Minimo:" , minimo)  
