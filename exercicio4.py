def fibonacci(x):
    if x == 0 or x == 1:
        return x
    return fibonacci(x - 1) + fibonacci(x - 2)

def fatorial(x):
    if x == 0 or x == 1:
        return 1
    return x * fatorial(x - 1)

def main():
    while True:
        try:
            x = int(input("Digite um número para calcular o Fatorial (ou -1 para sair): "))
            if x == -1:
                print("Encerrando o programa.")
                break
            if x < 0:
                print("Por favor, insira um número não negativo.")
            else:
                print("Fatorial:", fatorial(x))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    print("\nSequência de Fibonacci (primeiros 5 números):")
    for i in range(5):
        print(f"fibonacci({i}) = {fibonacci(i)}")

if __name__ == "__main__":
    main()
