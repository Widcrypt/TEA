try:
    file2read= input("Ingrese el nombre del archivo:")
    fhandle= open("mbox-short.txt", "r")
    for line in fhandle: 
        print(line.upper())
except:
    print("Error, archivo no encontrado")   
  
#print(fhandle.read().upper())  


