def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    
    precio = int(input("ingrese precio: "))#150
    descuento= float(input("ingrese descuento: ")) #23.5
    cantidad= float(input("ingrese la cantidad: ")) #3
    print("Precio: " + str(precio))
    print("Descuento: " + str(descuento))
    precio_descuento= precio - descuento
    print("Precio con descuento: " + str(precio_descuento))
    total = precio_descuento * cantidad
    print("Total: " + str(total))
    
if __name__ == '__main__':
    casting()