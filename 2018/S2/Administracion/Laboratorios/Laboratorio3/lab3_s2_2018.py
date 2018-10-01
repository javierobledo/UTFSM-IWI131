def limpiar_texto(texto, signos_puntuacion):
    for puntuacion in signos_puntuacion:
        texto = texto.replace(puntuacion,"")
    return texto.lower()

def abrir_archivo(nombre_archivo):
    archivo = open(nombre_archivo)
    lineas = []
    for linea in archivo:
        lineas.append(linea.strip())
    return " ".join(lineas)

def contar_palabras(texto):
    diccionario = {}
    palabras = texto.split()
    for palabra in palabras:
        if palabra not in diccionario:
            diccionario[palabra] = 0
        diccionario[palabra] += 1
    return diccionario

def ordenar_diccinario(diccionario):
    lista = []
    for k,v in diccionario.items():
        lista.append((v,k))
    lista.sort()
    lista.reverse()
    palabras = []
    for frec,palabra in lista:
        palabras.append(palabra)
    return palabras

puntuacion = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
libro = raw_input("Ingrese nombre del archivo del libro:")
while libro.lower() != "fin":
    texto = abrir_archivo(libro)
    texto = limpiar_texto(texto, puntuacion)
    frecuencia = ordenar_diccinario(contar_palabras(texto))
    n = int(raw_input("Ingrese n:"))
    for i in range(n):
        print frecuencia[i]
    libro = raw_input("Ingrese nombre del archivo del libro:")