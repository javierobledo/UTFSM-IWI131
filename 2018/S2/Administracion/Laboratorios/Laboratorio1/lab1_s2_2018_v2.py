import sys, time

def de_segundos_a_hora(segundos):
    h = str(segundos / 3600)
    m = str((segundos/60) % 60)
    s = str(segundos % 60)
    if len(h) == 1:
        h = "0"+h
    if len(m) == 1:
        m = "0"+m
    if len(s) == 1:
        s = "0"+s
    return h+":"+m+":"+s

def de_hora_a_segundos(hora):
    h = int(hora[0] + hora[1])
    m = int(hora[3] + hora[4])
    s = int(hora[6] + hora[7])
    return 3600*h + 60*m + s

tiempo = raw_input("Ingrese tiempo:")
segundos = de_hora_a_segundos(tiempo)
while segundos != 0:
    b = de_segundos_a_hora(segundos)
    sys.stdout.write('\r' + b)
    time.sleep(1)
    segundos -= 1
sys.stdout.write('\r' + "00:00:00")