def quien_gana(jugador1, jugador2):
    if jugador1 == jugador2:
        return 0
    elif jugador1 == "tijeras" and jugador2 == "piedra":
        return 2
    elif jugador1 == "tijeras" and jugador2 == "papel":
        return 1
    elif jugador1 == "tijeras" and jugador2 == "spock":
        return 2
    elif jugador1 == "tijeras" and jugador2 == "lagarto":
        return 1
    elif jugador1 == "papel" and jugador2 == "piedra":
        return 1
    elif jugador1 == "papel" and jugador2 == "tijeras":
        return 2
    elif jugador1 == "papel" and jugador2 == "spock":
        return 1
    elif jugador1 == "papel" and jugador2 == "lagarto":
        return 2
    elif jugador1 == "piedra" and jugador2 == "papel":
        return 2
    elif jugador1 == "piedra" and jugador2 == "tijeras":
        return 1
    elif jugador1 == "piedra" and jugador2 == "spock":
        return 2
    elif jugador1 == "piedra" and jugador2 == "lagarto":
        return 1
    elif jugador1 == "lagarto" and jugador2 == "papel":
        return 1
    elif jugador1 == "lagarto" and jugador2 == "tijeras":
        return 2
    elif jugador1 == "lagarto" and jugador2 == "spock":
        return 1
    elif jugador1 == "lagarto" and jugador2 == "piedra":
        return 2
    elif jugador1 == "spock" and jugador2 == "papel":
        return 2
    elif jugador1 == "spock" and jugador2 == "tijeras":
        return 1
    elif jugador1 == "spock" and jugador2 == "lagarto":
        return 2
    elif jugador1 == "spock" and jugador2 == "piedra":
        return 1

v1 = 0
v2 = 0
while v1 != 3 and v2 != 3:
    j1 = raw_input("Jugador 1:")
    j2 = raw_input("Jugador 2:")
    g = quien_gana(j1,j2)
    if g == 0:
        print "Empate"
    elif g == 1:
        print "Gana Jugador 1"
        v1 += 1
    elif g == 2:
        print "Gana Jugador 2"
        v2 += 1
    print "Jugador 1:",v1,"Jugador 2:",v2
if v1 > v2:
    print "VENCEDOR: Jugador 1"
else:
    print "VENCEDOR: Jugador 2"
