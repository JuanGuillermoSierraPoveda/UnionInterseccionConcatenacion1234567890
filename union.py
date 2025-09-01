L1 = {"a", "b", "ab", "ba"}
L2 = {"b", "c", "bc", "cb"}
L3 = {"a", "b", "c"}
L4 = {"ab", "ac"}
L5 = {"b", "bc", "ca", "c"}


def union_lenguajes(*lenguajes):
    resultado = set()
    for L in lenguajes:
        resultado |= set(L)
    return resultado


# Ejercicio 1
print("1) Calcula y muestra el resultado de la unión L1 y L2")
print("L1 ∪ L2 =", union_lenguajes(L1, L2))
# Ejercicio 2
print("2) Calcula y muestra el resultado de la unión L1 y L3")
print("L1 ∪ L3 =", union_lenguajes(L1, L3))
# Ejercicio 3
print("3) Calcula y muestra el resultado de la unión L2 y L3")
print("L2 ∪ L3 =", union_lenguajes(L2, L3))
# Ejercicio 4
print("4) Calcula y muestra el resultado de la unión L4 y L5")
print("L4 ∪ L5 =", union_lenguajes(L4, L5))
# Ejercicio 5
print("5) Calcula y muestra el resultado de la unión L1, L2 y L3")
print("L1 ∪ L2 ∪ L3 =", union_lenguajes(L1, L2, L3))
# Ejercicio 6
print("6) Crea dos lenguajes finitos y calcula su unión A∪B")
print("A = {'cad','aca','ad'}")
print("B = {'a','d','c'}")
A = {"cad", "aca", "ad"}
B = {"a", "d", "c"}
print("A ∪ B =", union_lenguajes(A, B))
# Ejercicio 7
print("7) Crea tres lenguajes finitos y calcula su unión A∪B∪C")
print("A = {'10','01','11'}")
print("B = {'0','1'}")
print("C = {'00','10'}")
A = {"10", "01", "11"}
B = {"0", "1"}
C = {"00", "10"}
print("A ∪ B ∪ C =", union_lenguajes(A, B, C))
# Ejercicio 8
print("8) Dado L1 y L2, calcula (L1 ∪ L2) y comprueba si la palabra 'abc' pertenece al resultado")
union_L1L2 = union_lenguajes(L1, L2)
print("(L1 ∪ L2) contiene 'abc'? ->", "abc" in union_L1L2)
# Ejercicio 9
print("9) Dado L4 y L5, calcula (L4 ∪ L5) y comprueba si la palabra 'a' pertenece al resultado")
union_L4L5 = union_lenguajes(L4, L5)
print("(L4 ∪ L5) contiene 'a'? ->", "a" in union_L4L5)
# Ejercicio 10
print("10) Usa la función union_lenguajes para realizar un ejemplo de prueba adicional")
L6 = {"x", "y"}
L7 = {"y", "z"}
print("L6 ∪ L7 =", union_lenguajes(L6, L7))
