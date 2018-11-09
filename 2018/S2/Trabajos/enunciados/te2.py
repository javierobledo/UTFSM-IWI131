def generar_reporte(diccio,lista):
    reporte = {}
    for profe, tareas in diccio.items():
        for tarea in tareas:
            if tarea not in lista:
                reporte[tarea] = {"cumple":[],"no cumple":[]}
            if (profe,tarea) in entregas:
                reporte[tarea]["cumple"].append(profe)
            else:
                reporte[tarea]["no cumple"].append(profe)
    return reporte