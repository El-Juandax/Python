llantas= int(input("¿Cuantas llantas compró usted?"))
precio_1= llantas * 300
precio_2= llantas * 250
precio_3= llantas * 200

if llantas < 5:
    print("El valor que debe pagar por las llantas es de:", precio_1)
    
elif llantas >= 5 and llantas < 10:
    print("El valor que debe pagar por las llantas es de:", precio_2)
    
elif llantas >= 10:
    print("El valor que debe pagar por las llantas es de:", precio_3)