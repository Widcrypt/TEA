file2read= input("Ingrese el nombre del archivo:")
fhandle= open(file2read, "r")
for line in fhandle:
    print(line.upper()) 

#print(fhandle.read().upper())  
