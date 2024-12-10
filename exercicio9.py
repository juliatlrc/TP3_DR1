class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def percorrer_em_ordem(no):
    if no is None:
        return []
    return (
        percorrer_em_ordem(no.esquerda) +
        [no.valor] +
        percorrer_em_ordem(no.direita)
    )


if __name__ == "__main__":
    raiz = No(20)
    raiz.esquerda = No(5)
    raiz.direita = No(15)
    raiz.esquerda.esquerda = No(2)
    raiz.esquerda.direita = No(4)
    raiz.direita.esquerda = No(12)
    raiz.direita.direita = No(10)

    valores = percorrer_em_ordem(raiz)
    print(valores)
