def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)

if __name__ == "__main__":
    lista = [2,1,10,5,4]
    lista_ordenada = quicksort(lista)
    print("Lista organizada:", lista_ordenada)
