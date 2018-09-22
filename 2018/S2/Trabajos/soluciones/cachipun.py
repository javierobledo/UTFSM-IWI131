from random import choice

jugador = raw_input("Ingrese su jugada [piedra/papel/tijera]:")
pc = choice(["piedra","papel","tijeras"])
print "El computador escoge",pc
if jugador == "piedra" and pc == "tijeras":
    print "Usted a ganado!"
elif jugador == "papel" and pc == "piedra":
    print "Usted a ganado!"
elif jugador == "tijeras" and pc == "papel":
    print "Usted a ganado!"
elif jugador == "papel" and pc == "tijeras":
    print "Gana el computador!"
elif jugador == "tijeras" and pc == "piedra":
    print "Gana el computador!"
elif jugador == "piedra" and pc == "papel":
    print "Gana el computador!"
elif jugador == pc:
    print "Empate!"
else:
    print "Jugada invalida!"