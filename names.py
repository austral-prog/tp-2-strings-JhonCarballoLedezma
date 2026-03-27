def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """

    """
    name = str(input("ingrese un nombre: "))
    last_name = str(input("ingrese un apellido: "))
    complete_name = name + last_name
    name_lower= complete_name.lower()
    name_title=complete_name.title()
    name_upper= complete_name.upper()
    name_tab= "\t" + name_lower
    print(name_lower)
    print(name_title)
    print(name_upper)
    print(name_tab)
    """
    nombre = input()
    apellido = input()
    nombre_completo = nombre + " " + apellido
    print(nombre_completo.lower)
    print(nombre_completo.title())
    print(nombre_completo.upper())
    print("\t" + nombre_completo.lower())
#names()