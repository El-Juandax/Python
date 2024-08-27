n_vendedores= int(input("Ingrese el numero de vendedores que hay "))
sueldo = int(input("Ingrese el sueldo de cada vendedor ")) 
ventas = 3
comision = 0.10

for vendedor in range(1, n_vendedores + 1):
    
    ventas_realizadas = int(input("Digite el valor de las ventas que realizo "))
    comision_ventas = ventas_realizadas * comision
    salario_total = sueldo + comision_ventas
    print(salario_total)
    

