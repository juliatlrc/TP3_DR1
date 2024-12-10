def contar_repeticoes(string, caractere, indice=0):
    if indice == len(string):
        return 0
    return (1 if string[indice] == caractere else 0) + contar_repeticoes(string, caractere, indice + 1)


if __name__ == "__main__":
    string = "banana"
    caractere = "a"
    resultado = contar_repeticoes(string, caractere)
    print(f"{resultado} repetições ")