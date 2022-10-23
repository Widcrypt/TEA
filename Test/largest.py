largest = None 
print('Before', largest)

for i in [4,78,34,12,90,178,43]: 
    if largest is None or i > largest : 
        largest = i 
        print('Loop:', i, largest)
print('Largest:', largest) 
 