import os

def listar_diretorios(caminho):
    elementos = []
    for item in os.listdir(caminho):
        item_caminho = os.path.join(caminho, item)
        if os.path.isdir(item_caminho):
            elementos.append(f"Diretório: {item_caminho}")
            elementos.extend(listar_diretorios(item_caminho))
        else:
            elementos.append(f"Arquivo: {item_caminho}")
    return elementos


if __name__ == "__main__":
    caminho_base = "teste_diretorios"
    conteudo = listar_diretorios(caminho_base)
    for elemento in conteudo:
        print(elemento)
