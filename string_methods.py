def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""
    
    nombre_sin_espacio = nombre.strip()
    nombre_sin_espacioI = nombre.lstrip()
    nombre_sin_espacioD = nombre.rstrip()
    frase_upper=frase.upper()
    frase_lower= frase.lower()
    frase_title=frase.title()
    posicion = frase.find("gran")
    reemplazar = frase.replace("programacion","desarrollo")
    contar_a = frase.count("a")
    palabra_esta1 = "Python" in frase
    palabra_esta2 = "Java" in frase
    extraer = f"{"Python"}"
    caracter_no_contiguo_python= f"{frase [0:6:2]}"
    caracter_inverso_python= f"{frase[5::-1]}"
    formato= f"{nombre_sin_espacio} sabe {extraer}"
    line_1= multilinea[0:7]
    line_2= multilinea[12:19]
    line_3= multilinea[24:31]
    
    print(f'Strip: {nombre_sin_espacio}')
    print(f'Lstrip: {nombre_sin_espacioI}')
    print(f'Rstrip: {nombre_sin_espacioD}')
    print(f'Upper: {frase_upper}')
    print(f'Lower: {frase_lower}')
    print(f'Title: {frase_title}')
    print(f'Find: {posicion}')
    print(f'Replace: {reemplazar}')
    print(f'Count: {contar_a}')
    print(f'Contiene Python: {palabra_esta1}')
    print(f'Contiene Java: {palabra_esta2}')
    print(f'Slice: {extraer}')
    print(f'Paso: {caracter_no_contiguo_python}')
    print(f'Reverso: {caracter_inverso_python}')
    print(f'Formato: {formato}')
    print(line_1)
    print(line_2)
    print(line_3)


#string_methods()