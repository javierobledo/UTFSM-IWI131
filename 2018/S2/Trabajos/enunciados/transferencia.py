personas = {"1234567-8":"hol34as"}
letras = "abcdefghijklmnopqrstuvwxyz"
digitos = "0123456789"

def f1(rut):
    suma = 0
    i=2
    rutinverso = rut[::-1]
    for digito in rutinverso:
        suma += int(digito)*i
        if i == 7:
            i = 1
        i += 1
    d = 11-(suma%11)
    if d == 11:
        return "0"
    elif d == 10:
        return "k"
    else:
        return str(d)



def es_letra(simbolo):
    return simbolo in letras

def es_numero(simbolo):
    return simbolo in digitos

def rut_valido(rut):
    i = rut.index("-")
    rutsindigito = rut[:i]
    digito = rut[i+1:]
    return f1(rutsindigito) == digito

def codificar_password(password):
    return

def decodificar_password(password):
    return


rut = raw_input("Ingrese rut:")
while rut != "0":
    while not rut_valido(rut):
        print "Rut invalido!"
        rut = raw_input("Ingrese rut:")
    password = raw_input("Password:")
    if rut in personas:
        if decodificar_password(personas[rut]) == password:
            print "Password correcto, puede ingresar al sistema"
        else:
            print "Password incorrecto!"
    else:
        personas[rut] = codificar_password(password)
        print "Persona ingresada correctamente"
    rut = raw_input("Ingrese rut:")