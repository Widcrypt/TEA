notas = float(input('Ingrese nota:'))

if notas<0 and notas>1:
        print('Fuera de rango!!. Debe ser entre 0.0 y 1.0')
else:
        if notas >= 0.9:
            print('Sobresaliente')
        if notas >= 0.8 and notas < 0.9:
            print('Notable')
        if notas >= 0.7 and notas < 0.8:
            print('Bien')
        if notas >= 0.6 and notas < 0.7:
            print('Suficiente')

