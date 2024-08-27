num_alumnos = int(input("Digite la cantidad de alumnos"))
contador_alumnos = 0


for alumnos in range(1, num_alumnos + 1):
    total_calificaciones = 0
    alumno = input("Nombre del alumno ")
    num_calif = int(input("Ingrese el numero de calificaciones que hay"))
    
    for calificacion in range (1, num_calif + 1):
        calificacion = float(input("Ingrese la calificacion"))
        total_calificaciones = total_calificaciones + calificacion
        
    prom =  total_calificaciones / num_calif
    
    if prom <= 3.4 :
        print(alumno, "Tiene que presentar el examen de recuperacion, su nota es:", prom)
        contador_alumnos= contador_alumnos + 1
        
    else :
        print(alumno, "No tiene que presentar el examen, su nota es:", prom) 

print("La cantidad de alumnos que tienen que presentar examen es de:", contador_alumnos) 