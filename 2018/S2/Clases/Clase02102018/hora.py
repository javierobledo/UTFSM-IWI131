hora = raw_input("Ingrese la hora en formato hh:mm:ss :")
h = int(hora[0]+hora[1])
m = int(hora[3]+hora[4])
s = int(hora[6]+hora[7])
segundos = 3600*h + 60*m + s
print "Los cantidad de segundos es", segundos