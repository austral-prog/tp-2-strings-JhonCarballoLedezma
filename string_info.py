def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    
    print(f"Palabra: {palabra}")
    cant_palabra = len(f"{palabra}")
    print(f"Longitud: {cant_palabra}")
    primer_letra= palabra[0]
    print(f"Primera letra: {primer_letra}")
    ultima_letra = palabra[-1]
    print(f"Ultima letra: {ultima_letra}")
    repite_3= palabra * 3
    print( f"Repetida: {repite_3}")
    adorno= f"***{palabra}***"
    print(f"Decorada: {adorno}")

#string_info()