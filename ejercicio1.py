# Ejercicio 1: Utilice las funciones anteriores para agregar elementos falatantes.

lista = ["P", "t"]
lista.insert(1,"y")
lista.extend(["h","o","n"])
print("lista = ", lista)
assert "".join(lista) == "Python"