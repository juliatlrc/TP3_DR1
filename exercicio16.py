def inverter_string(string, inicio=0):
    if inicio == len(string):
        return ""
    return inverter_string(string, inicio + 1) + string[inicio]

if __name__ == "__main__":
    string = "recursao"
    resultado = inverter_string(string)
    print(f"A string invertida de '{string}' é '{resultado}'")
