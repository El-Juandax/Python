num_estudiantes = 5
contador_menor_a_50 = 0
contador_menor_a_70 = 0
contador_menor_a_80 = 0
contador_mayor_a_80 = 0

for estudiante in range(1, num_estudiantes + 1):
    calificacion = int(input("¿Cual fue su calificacion en el examen? ") )
    
    if calificacion < 50 :
        print("Perdio el examen")
        contador_menor_a_50 = contador_menor_a_50 + 1
        
    elif calificacion >= 50 and calificacion < 70 :
        print("Perdio el examen")
        contador_menor_a_70 = contador_menor_a_70 + 1
        
    elif calificacion >= 70 and calificacion < 80 :
        print("!Paso el examen¡") 
        contador_menor_a_80 = contador_menor_a_80 + 1
        
    elif calificacion >= 80 :
        print("!Paso el examen¡")
        contador_mayor_a_80 = contador_mayor_a_80 + 1
        
print("La cantidad de estudiantes que tuvieron una calificaion menor a 50 es de:", contador_menor_a_50)
print()
print("La cantidad de estudiantes que tuvieron una calificaion entre 50 y 70 es de:", contador_menor_a_70)
print()
print("La cantidad de estudiantes que tuvieron una calificaion entre 70 y 80 es de:", contador_menor_a_80)
print()
print("La cantidad de estudiantes que tuvieron una calificaion mayor a 80 es de:", contador_mayor_a_80)


