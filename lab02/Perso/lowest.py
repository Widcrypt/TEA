lowest = None 
print("Antes: ", lowest)
for i in [3, 41, 12, 9, 74, 15]:
     if lowest is None or i < lowest:
         lowest = i
     print("Loop: ", i, lowest)
print(lowest)  