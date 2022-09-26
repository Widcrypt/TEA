nota = float(input('Introduzca puntuacion:')) 
if nota < 0.0 or nota > 1.0:  
    print('Punctuación incorrecta')
else:
    if nota > 0.9:
        print('Sobresaliente')
    elif 0.8< nota <= 0.9:
        print('Notable')
    elif 0.7 < nota <= 0.8:
        print('Bien')
    elif 0.6<= nota < 0.7:
        print('Suficiente')
    elif nota <= 0.6: 
        print('Insuficiente')  