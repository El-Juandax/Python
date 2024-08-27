votos = 2500000 
contador_candidato_1 = 0
contador_candidato_2 = 0
contador_candidato_3 = 0
nom_candidato_1 = "Benjamin Byron Davis"
nom_candidato_2 = "Roger Clark"
nom_candidato_3 = "Peter Blomcuist"

for candidatos in range(1, votos + 1):
    voto_candidato = int(input("¿Cual es el numero de tarjeton del candidato por el que quiere votar? "))
    
    if voto_candidato == 1 :
        print("Voto registrado")
        contador_candidato_1 = contador_candidato_1 + 1
    elif voto_candidato == 2 :
        print("Voto registrado")
        contador_candidato_2 = contador_candidato_2 + 1
    elif voto_candidato == 3 :
        print("Voto registrado")
        contador_candidato_3 = contador_candidato_3 + 1

if contador_candidato_1 > contador_candidato_2 and contador_candidato_1 > contador_candidato_3 :
        print("El candidato", nom_candidato_1, "Es el ganador")
        
elif contador_candidato_2 > contador_candidato_1 and contador_candidato_2 > contador_candidato_3 :
        print("El candidato", nom_candidato_2, "Es el ganador")
    
elif contador_candidato_3 > contador_candidato_2 and contador_candidato_3 > contador_candidato_1 :
        print("El candidato", nom_candidato_3, "Es el ganador")
        
