def soma_recursiva(lista, indice=0):
    if indice == len(lista):
        return 0
    return lista[indice] + soma_recursiva(lista, indice + 1)

if __name__ == "__main__":
    resultado = soma_recursiva([1, 2, 3, 4])
    print(f"Soma dos elementos da lista: {resultado}")
