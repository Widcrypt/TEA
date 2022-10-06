file2read= input("Ingrese el nombre del archivo:")
fhandle= open("temperatura.txt", "r")
for line in fhandle:
    print(line.upper())   

#print(fhandle.read().upper())  
