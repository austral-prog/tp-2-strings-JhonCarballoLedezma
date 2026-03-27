def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"
    texto_lower=texto.lower()
    texto_3= texto_lower[0:3]
    texto_2_4= texto_lower[2:5]
    print(texto_3)
    print(texto_2_4)
    print(texto_lower)
    

#slice_simple()