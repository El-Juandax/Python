n_clientes = int(input("¿Cuantos clientes hubo en el dia? "))

rojo = 0.4
amarilla = 0.25
blanca = 0

for cliente in range(1, n_clientes + 1):
    
     valor_a_pagar = int(input("Ingrese el valor de la compra del cliente "))
     bolita = input("¿De que color es la bolita que saco? ")
     
     if bolita == "Rojo" or bolita == "rojo" or bolita == "ROJO" :
         descuento_1 = valor_a_pagar -(valor_a_pagar * rojo)
         print("El descuento es de: ", descuento_1)
         print()
         
     elif bolita == "Amarillo" or bolita== "amarillo" or bolita == "AMARILLO" :
         descuento_2 = valor_a_pagar - (valor_a_pagar * amarilla)
         print("El descuento es de", descuento_2)
         print()
         
     elif bolita == "Blanco" or bolita == "blanco" or bolita == "BLANCO" :
         print("No tiene descuento", valor_a_pagar) 
         print()
                 
