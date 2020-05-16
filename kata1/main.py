

"""

#parte 1

precio = 3.49
descuento = 0.6

print("cuantas barras no son del dia?")
barras_no_frescas = int(input())
precio_no_fresco= precio*(1-descuento)

print("El precio normal es de "+str(precio)+"€ pero con descuento se te queda a "+str(precio_no_fresco)+"€")
print("El total de ingresos del dia es de "+ str(precio_no_fresco*barras_no_frescas))

"""

"""

#parte 2
password = "helloworld"

inputed_password = input("escriba su contraseña\n").lower()

if password == inputed_password:
    print("logged in")
else:
    print("contraseña incorrecta")

"""

"""
#parte 3
edad = int(input("cuantos años tiene?\n"))
if edad <4:
    print("entrada gratis")
elif edad <18:
    print("entrada cuesta 5€")
else:
    print("entrada cuenta 10€")
    """