def max(listaTuplas,pesoTotal):
    tam = len(listaTuplas)
    if tam>0:
        tupla = listaTuplas[tam - 1]
        peso = tupla[0]
        nuevoPeso = pesoTotal - peso
        if nuevoPeso>=0:
            listaTuplas = listaTuplas[:tam-1]
            x = [tupla]+max(listaTuplas,nuevoPeso)
            y = []+max(listaTuplas,nuevoPeso)

            costo1 = 0
            costo2 = 0

            for i in x:
                costo1 += i[1]
            for i in y:
                costo2 += i[1]

            if costo1>costo2:
                return x
            else:
                return y
        else:
            #En caso que el nuevo peso no entre, se llama recursivamente a la función pero disminuido en la lista de tuplas y con el peso original desde donde es llamada
            return max(listaTuplas[:tam-1],pesoTotal)
    else:
        return []

