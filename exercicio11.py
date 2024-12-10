def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

if __name__ == "__main__":
    try:
        print(fatorial(1000))
    except RecursionError as e:
        print("Erro de recursão:", e)


def fatorial_cauda(n, acumulador=1):
    if n == 0 or n == 1:
        return acumulador
    return fatorial_cauda(n - 1, acumulador * n)


if __name__ == "__main__":
    try:
        print(fatorial_cauda(1000))
    except RecursionError as e:
        print("Erro de recursão:", e)
