computadores = int(input("¿Cuantas computadoras compro usted?"))
precio_computadores = 11000
valor_total = precio_computadores * computadores
descuento_1 = valor_total - (valor_total * 0.1)
descuento_2 = valor_total - (valor_total * 0.2)
descuento_3 = valor_total - (valor_total * 0.4)

if computadores < 5:
    print("el numero de computadores comprados es de:", computadores)
    print("el precio original de los computadores es de:", valor_total)
    print("el descuento es de 10%")
    print("el valor total es de:", descuento_1)
    
elif computadores >= 5 and computadores < 10 : 
    print("el numero de computadores comprados es de:", computadores)
    print("el precio original de los computadores es de:", valor_total)
    print("el descuento es de 20%")
    print("el valor total es de", descuento_2)
    
elif computadores >= 10:
    print("el numero de computadores comprados es de:", computadores)
    print("el precio original de los computadores es de:", valor_total)
    print("el descuento es de 40%")
    print("el valor total es de", descuento_3)  