kilo_manzana = float(input("¿Cuantos kilos de manzana compro?"))
precio = int(input("¿Cual fue el precio a pagar?"))
descuento_1 = precio - (precio * 0.1)
descuento_2 = precio - (precio * 0.15)
descuento_3 = precio - (precio * 0.2)

if kilo_manzana > 0 and kilo_manzana <= 2 :
    print("No tiene descuento")
    
elif kilo_manzana >= 2.01 and kilo_manzana <= 5 :
    print("El precio con descuento es de:", descuento_1)
    
elif kilo_manzana >= 5.01 and kilo_manzana <= 10 :
    print("El precio con descuento es de: ", descuento_2)
    
elif kilo_manzana >= 10.01 :
    print("El precio con descuento es de: ", descuento_3)    