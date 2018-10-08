fecha = raw_input("Ingrese fecha:")
mayor = -float("inf")
menor = float("inf")
while fecha != "0":
    calorias_diarias = 0
    n = int(raw_input("Cuantos ejercicios hizo el dia?:"))
    i = 1
    while i <= n:
        ejercicio = raw_input("Nombre del ejercicio:")
        calorias = int(raw_input("Calorias quemadas:"))
        if calorias >  mayor:
            mayor = calorias
            nombre_ejercicio = ejercicio
            dia_ejercicio = fecha
        calorias_diarias += calorias
        i += 1
    if calorias_diarias < menor:
        menor = calorias_diarias
        fecha_menor = fecha
    fecha = raw_input("Ingrese fecha:")
print "El ejercicio mas potente fue",ejercicio,"realizado el",dia_ejercicio,"quemando",mayor,"calorias"
print "El dia donde se quemaron menos calorias fue el",fecha_menor,"donde se quemaron",menor,"calorias"