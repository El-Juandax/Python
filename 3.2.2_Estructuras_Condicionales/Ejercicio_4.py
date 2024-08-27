precio = int(input("Coloque el precio por el que compro el aparato: "))
marca = input("Coloque la marca del objeto: ")
precio_sin_iva = precio - (precio * 0.21)
descuento_1 = precio_sin_iva - (precio_sin_iva * 0.10) 
descuento_2 = precio_sin_iva - (precio_sin_iva * 0.05)
descuento_3 = precio_sin_iva - (precio_sin_iva * 0.05) - (precio_sin_iva * 0.10) 


if precio > 20000 :

    print("El descuento es de:", descuento_1)
    
    if marca == "Nosy" :

        print("El descuento es de:", descuento_3)
    
else:
    print("el aparato no tiene descuento de precio")
    
if marca == "Nosy" :

    print("El descuento es de:", descuento_2)

else:
    print("el aparato no tiene descuento de marca")
    

    