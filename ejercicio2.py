# Ejercicio 2: Utilice las funciones anteriores para elminar elementos sobrantes.

lista = [1,4,2,5,4,3,4,7,5,8,9]
del lista [9:]
del lista [7]
del lista [4]
del lista [3]
del lista [1]

print("lista es =",lista)
assert lista == list(range(1, 6))
