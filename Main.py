if __name__ == '__main__':
    from ClaseConjunto import conjunto
    from Funciones import carga
    from Funciones import menu
    listaObj = []
    #i = int(input("Ingrese la cantidad de conjuntos a cargar: "))
    for k in range(2):
        lista = carga(k)
        nuevoObjeto = conjunto(lista)
        listaObj.append(nuevoObjeto)
    
    menu(listaObj)
    
    
    
