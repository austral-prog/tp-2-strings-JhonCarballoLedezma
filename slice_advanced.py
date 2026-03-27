def slice_advanced():
    """Lee un texto e imprime los caracteres desde la posición 4
    en adelante, tomando uno de cada dos (paso 2).
    """
    pass
    texto=input("ingrese texto: ")
    texto_lee= texto[4::2]
    print(texto_lee)

if __name__ == '__main__':
    slice_advanced()