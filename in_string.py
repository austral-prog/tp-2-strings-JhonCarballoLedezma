def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    pass
    nombre=input("ingrese su nombre: ")
    nombre_lower=nombre.lower()
    contiene_a= "a" in nombre_lower
    contiene_e= "e" in nombre_lower
    contiene_i= "i" in nombre_lower
    contiene_o= "o" in nombre_lower
    contiene_u="u" in nombre_lower
    
    print(f"Contiene a: {contiene_a}")
    print(f"Contiene e: {contiene_e}")
    print(f"Contiene i: {contiene_i}")
    print(f"Contiene o: {contiene_o}")
    print(f"Contiene u: {contiene_u}")


check_vowels()