modismos = {"Chile": {"Viejito", "Pascuero", "po", "altiro"},
          "Brasil": {"Papai", "Noel", "moro", "quero", "anos", "Adeus"},
          "Costa Rica": {"Colacho", "vivo", "deseo", "agnos", "Adios"}}

def lista_regalos(cartas):
    for c in cartas:
        p = set()
        arch = open(c)
        clinea = 0
        for l in arch:
            l = l.replace(".", "")
            l = l.replace(",", "")
            if clinea == 3:
                reg = l.strip()
            p = p |set(l.strip().split())
            clinea += 1
        arch.close()
        nom = l.strip()
        pais = obtener_pais(p,modismos)
        archpais = open(pais+".csv","a")
        archpais.write(nom+";"+reg+"\n")
        archpais.close()

def obtener_pais(palabras,modismos):
    may = 0
    for p,ppais in modismos.items():
        cantp = len(palabras & ppais)
        if may < cantp:
            may = cantp
            paisprobable = p
    return paisprobable
