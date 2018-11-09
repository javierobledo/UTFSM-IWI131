def f1(x,j=-1):
    y = []
    for i in range(j,-len(x)+j,j):
        y.append(x[i])
    return y

def digito_verificador(rut):
    suma = 0
    i=2
    rutinverso = f1(rut)
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


def rut_valido(rut):
    i = rut.index("-")
    rutsindigito = rut[:i]
    digito = rut[i+1:]
    return digito_verificador(rutsindigito) == digito

personas = {}
rut = raw_input("Ingrese rut:")
while rut != "0":
    while not rut_valido(rut):
        print "Rut invalido!"
        rut = raw_input("Ingrese rut:")
    password = raw_input("Password:")
    if rut in personas:
        if personas[rut] == password:
            print "Password correcto, puede ingresar al sistema"
        else:
            print "Password incorrecto!"
    else:
        personas[rut] = password
        print "Persona ingresada correctamente"
    rut = raw_input("Ingrese rut:")
print "Ruts en el sistema:"
for rut in personas:
    print rut