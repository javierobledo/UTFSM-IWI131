#valentia,inteligencia,bondad

princesas = {"mulan":(10,10,5),"tiana":(5,5,5),"leia":(10,10,2),"ariel":(5,7,10),"belle":(5,10,10),"elsa":(4,7,4),"pocahontas":(10,10,10),"rapunzel":(6,6,8)}

def distancia(p1,p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5

def ordena_mis_princesas(valentia,inteligencia,bondad,princesas):
    distancias = []
    for princesa,atributos in princesas.items():
        distancias.append((distancia((valentia,inteligencia,bondad),atributos), princesa))
    distancias.sort()
    nombres = []
    for _, princesa in distancias:
        nombres.append(princesa)
    return nombres