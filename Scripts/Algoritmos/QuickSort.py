# le hago sort alfabetico  a lista de pisos
def quickSort(lista):
    longitud = len(lista)
    if longitud <= 1:
        return lista
    else:
        pivote = lista.pop()
    elementos_mayores = []
    elementos_menores = []
    for elemento in lista:
        # comparo el valor ascii de los caracteres
        if ord(elemento.datos.nombre) > ord(pivote.datos.nombre):
            elementos_mayores.append(elemento)
        else:
            elementos_menores.append(elemento)

    return quickSort(elementos_menores) + [pivote] + quickSort(elementos_mayores)



