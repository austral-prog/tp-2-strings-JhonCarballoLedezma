def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    
    nombre_completo = (input("Ingrese un nombre completo: ").rstrip()).lstrip()
    email = input("Ingrese un email: ")
    tres_notas = [str(input("Ingrese la 1era nota: ")), str(input("Ingrese la 2da nota: ")), str(input("Ingrese la 3ra nota: "))]

    encabezado_decorativo =  """========================
    FICHA DEL ALUMNO
========================"""

    nombre = input("Ingrese nombre completo: ")
    nombre = nombre.title()
    nombre = nombre.strip()
    email = input("Ingrese email: ")
    email = email.lower()
    nota1 = int(input("Ingrese nota: "))
    nota2 = int(input("Ingrese nota: "))
    nota3 = int(input("Ingrese nota: "))

    print(f"========================\n    FICHA DEL ALUMNO\n========================")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Caracteres en nombre: {len(nombre)}")
    space_middle = nombre.find(' ')
    iniciales_nombre = nombre[0] + nombre[space_middle + 1]
    print(f"Iniciales: {iniciales_nombre}")
    usuario = (nombre[space_middle + 1:] + "." + nombre[0:space_middle]).lower()
    print(f"Usuario: {usuario}")
    print(f"Email valido: {'@' in email}")
    dominio = email[ email.find('@')+1:]
    print(f"Dominio: {dominio}")
    usuario_guion = nombre[0:space_middle] + "" + nombre[space_middle + 1:]
    print(f"Nombre para archivo: {usuario_guion}")
    print(f"Cantidad de a: {nombre.count('a')}")
    codigo_secreto = nombre[::-1].upper()
    print(f"Codigo secreto: {codigo_secreto}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    suma_notas = nota1 + nota2 + nota3
    print(f"Suma: {suma_notas}")
    promedio_notas = suma_notas/3
    print(f"Promedio: {promedio_notas}")
    promedio_entero = suma_notas //3
    print(f"Promedio entero: {promedio_entero}")
    print(f"========================")

#ficha()