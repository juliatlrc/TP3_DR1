def eh_palindromo(palavra, acumulador=True):
    if len(palavra) <= 1 or not acumulador:
        return acumulador
    if palavra[0] != palavra[-1]:
        return False
    return eh_palindromo(palavra[1:-1], acumulador)

if __name__ == "__main__":
    palavras = ["arara", "lual", "julia", "arara", "osso"]
    for palavra in palavras:
        resultado = eh_palindromo(palavra)
        print(f"{palavra}' é um palíndromo?? {'Sim' if resultado else 'Não'}")
