def particionar(lista, esquerda, direita):
    pivo = lista[direita]
    i = esquerda
    for j in range(esquerda, direita):
        if lista[j] < pivo:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
    lista[i], lista[direita] = lista[direita], lista[i]
    return i

def quick_select(lista, esquerda, direita, k):
    indice_pivo = particionar(lista, esquerda, direita)
    if indice_pivo == k - 1:
        return lista[indice_pivo]
    elif indice_pivo > k - 1:
        return quick_select(lista, esquerda, indice_pivo - 1, k)
    else:
        return quick_select(lista, indice_pivo + 1, direita, k)


if __name__ == "__main__":
    lista = [34,3,21,2,55,6]
    k = 2
    resultado = quick_select(lista, 0, len(lista) - 1, k)
    print(f"resultado => {resultado}")
