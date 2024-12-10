def somar_elementos(lista, indice=0):
    if indice == len(lista):
        return 0
    return lista[indice] + somar_elementos(lista, indice + 1)

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    resultado = somar_elementos(lista)
    print(f"Soma dos elementos da lista: {resultado}")

