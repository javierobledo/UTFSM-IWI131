def cuantos_segundos(hora_en_string):
    h = int(hora[0] + hora[1])
    m = int(hora[3] + hora[4])
    s = int(hora[6] + hora[7])
    return 3600 * h + 60 * m + s

def primo(n):
    i = 2
    es_primo = True
    while i < n:
        if n % i == 0:
            es_primo = False
        i += 1
    return es_primo

hora = raw_input("Ingrese hora:")
while hora != "fin":
    hora = raw_input("Ingrese hora:")
    if primo(cuantos_segundos(hora)):
        print "Las",hora,"es una hora segura"
    else:
        print "No salgas de tu casa!"