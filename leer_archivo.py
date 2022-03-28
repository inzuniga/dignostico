import json


def leer_archivo(archivo):

    lista = list()
    with open(archivo) as file:
        linea = file.readline()

        while linea != "":
            final = json.loads(linea.strip())
            lista.append(final)
            linea = file.readline()
    return lista