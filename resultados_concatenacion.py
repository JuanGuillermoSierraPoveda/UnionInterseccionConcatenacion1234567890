# Rama 3: Concatenación de Lenguajes
# Función genérica para concatenar dos lenguajes
def concatenacion_lenguajes(L1, L2):
    resultado = set()
    for x in L1:
        for y in L2:
            resultado.add(x + y)
    return resultado

# Función para comprobar si una palabra está en el lenguaje
def comprobar(L, palabra):
    if palabra in L:
        print(f"La palabra '{palabra}' SÍ pertenece al lenguaje.")
    else:
        print(f"La palabra '{palabra}' NO pertenece al lenguaje.")


# ------------------------------
# Definición de lenguajes base
# ------------------------------
L1 = {"a", "b", "ab", "ba"}
L2 = {"b", "c", "bc", "cb"}
L3 = {"a", "b", "c"}
L4 = {"ab", "ac"}
L5 = {"b", "bc", "ca", "c"}

# 1. Concatenación L1 · L3
res1 = concatenacion_lenguajes(L1, L3)
print("Ejercicio 1 (L1·L3):", res1)

# 2. Concatenación L3 · L1
res2 = concatenacion_lenguajes(L3, L1)
print("Ejercicio 2 (L3·L1):", res2)

# 3. Concatenación L4 · L5
res3 = concatenacion_lenguajes(L4, L5)
print("Ejercicio 3 (L4·L5):", res3)

# 4. Concatenación L5 · L4
res4 = concatenacion_lenguajes(L5, L4)
print("Ejercicio 4 (L5·L4):", res4)

# 5. Concatenación L1 · L2
res5 = concatenacion_lenguajes(L1, L2)
print("Ejercicio 5 (L1·L2):", res5)

# 6. A={"a","b"} y B={"a","c"}
A = {"a", "b"}
B = {"a", "c"}
res6 = concatenacion_lenguajes(A, B)
print("Ejercicio 6 (A·B):", res6)

# 7. A={"0","1"} y B={ε,"00"} (ε es cadena vacía)
A = {"0", "1"}
B = {"", "00"}  # "" representa ε
res7 = concatenacion_lenguajes(A, B)
print("Ejercicio 7 (A·B con ε):", res7)

# 8. (L1 · L2) comprobar si "aba" pertenece
res8 = concatenacion_lenguajes(L1, L2)
print("Ejercicio 8 (L1·L2):", res8)
comprobar(res8, "aba")

# 9. (L3 · L4) comprobar si "cab" pertenece
res9 = concatenacion_lenguajes(L3, L4)
print("Ejercicio 9 (L3·L4):", res9)
comprobar(res9, "cab")

# 10. Ejemplo adicional de prueba
A = {"x", "y", "z"}
B = {"m", "n", "z"}
res10 = concatenacion_lenguajes(A, B)
print("Ejercicio 10 (A·B extra):", res10)
