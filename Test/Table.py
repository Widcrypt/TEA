# 1.1 AND
A = False
B = False
C = A and B
print("Tabla de Verdad para el Operador Logico AND")
print("===========================================")
print("|     A     |       B      |    A and B   |")
print("|-----------------------------------------|")
print("|  ", A, "  |   ", B, "    |   ", C, "    |")
print("|  ", False, "  |   ", True, "     |   ", False and True, "    |")
A = True
B = False
C = A and B
print("|  ", A, "   |   ", B, "    |   ", C, "    |")
A = True
B = True
C = A and B
print("|  ", A, "   |   ", B, "     |   ", C, "     |")
# new line caracter de escape
print("|-----------------------------------------|\n")