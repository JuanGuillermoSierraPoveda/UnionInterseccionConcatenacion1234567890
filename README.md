# ACTIVIDAD CADI: OPERACIONES CON LENGUAJES FINITOS

## Resumen del trabajo

Inicialmente, el docente nos indica que apropiemos los conocimientos de Lenguajes y Conjuntos. Esto enfocándolo en realizar operaciones de lenguajes finitos (unión, intersección y concatenación) en conjunto con hacer colaboración en grupo utilizando Git.

El gestor de conocimiento nos da cinco conjuntos de lenguajes que vamos a empezar a definir:

```python
L1 = {"a", "b", "ab", "ba"}
L2 = {"b", "c", "bc", "cb"}
L3 = {"a", "b", "c"}
L4 = {"ab", "ac"}
L5 = {"b", "bc", "ca", "c"}
```

## Roles

Se reunieron los seres actuantes y transformadores:

Juan Guillermo Julio Lee Sierra Poveda
Juan David Navarrete Niño
David Santiago Riaño Fuquene

Con el fin de llevar a cabo el trabajo asignado por el gestor de conocimiento durante el espacio de aprendizaje. 

Juan Guillermo Julio Lee Sierra Poveda, lider y Scrum Manager, se encargó de la organización de la actividad, de la asignación de trabajo, de la solución de la rama #1 del trabajo con referecia a la unión de lenguajes finitos y de disponer los elementos con el fin de facilitar la interación entre los miembros participantes

Juan David Navarrete Niño, sub-Scrum Manager del trabajo, se encargó de la solución y respuesta referente a los ejercicios enfoncados en intersección como operaciones fundamentes de los lenguajes finitos. 

David Santiago Riaño Fuquene en encargo de la 3 rama que es la que corresponde a la operacion de el lenguajes formales de las otras dos ramas anteoriores

Finalmente, los tres llevamos a cabo la complicidad del documento README.md, incluyendo su debida documentación e instrucción para clonar el repositorio y ejecutar los scripts solicitados para ver sus correspondientes resultados.

## Union

En el ejercicio de union, vamos a reconocer los elementos compartidos entre lenguajes, e imprimirlos.
La función usada en dicho ejercicio es la siguiente:

```python
def union_lenguajes(*lenguajes):
    resultado = set()
    for L in lenguajes:
        resultado |= set(L)
    return resultado
```

Empezamos definiendo la función *union_lenguajes()* la cual va a recibir los grupos de lenguajes que vamos a unir. Pero cómo puede que recibamos dos o tres lenguajes, utilizamos **lenguajes* para indicar que la cantidad de entradas puede variar.
Seguido, definimos el conjunto final *resultado = set()*, para que almacene la unión de todos los lenguajes.
Ya con esto, recurrimos a un ciclo for para que recorra cada elemento de cada grupo y con ayuda del operador **|=** indicamos que vamos a unir los conjuntos en uno solo.

Ahora, podemos coger como ejemplo, el ejercicio #1

```python
print("1) Calcula y muestra el resultado de la unión L1 y L2")
print("L1 ∪ L2 =", union_lenguajes(L1, L2))
```

Aquí podemos identificar que solo debemos llamar a la funcion *union_lenguajes* e indicarle los *arrays* que queremos unir.

Ahora, los ejercicios del 1 al 5 son así, pero los 6 y 7 son diferentes

```python
print("6) Crea dos lenguajes finitos y calcula su unión A∪B")
print("A = {'cad','aca','ad'}")
print("B = {'a','d','c'}")
A = {"cad", "aca", "ad"}
B = {"a", "d", "c"}
print("A ∪ B =", union_lenguajes(A, B))
```

Se nos solicita crear otros dos lenguajes finitos y unirlos, pero como podemos evidenciar, no resultó ser un gran problema. 
Sin embargo, los ejercicios 8, 9 y 10 nos piden identificar si dentro de la unión, cierto elemento se encuentra o no. La solución que apropiamos fue la siguiente:

```python
print("(L1 ∪ L2) contiene 'abc'? ->", "abc" in union_L1L2)
```

Los comandos de Git usados para la solución de esta primera parte de la actividad fueron:

```bash
git init
git status
git pull 
git add nombre_del_documento
git reset nombre_del_documento
git commit -m "comentario de guardado"
git branch -M master main
git push
```

## Interseccion

El ejercicio de interseccion consiste en reconocer los elementos compartidos entre lenguajes, e imprimirlos, las funciones usadas en este ejercicio son estas:

```python
#Funcion para comparar ambos diccionarios y crear uno con los elementos el comun
def inter(dicx,dicy):
    dicf=[]
    #Se imprimen los lenguajes que se van a usar para dejarlo claro al usuario
    print("\nLenguajes para interseccion\n%s\n%s"%(dicx,dicy))
    for x in range(0,len(dicx)):
        for y in range(0,len(dicy)):
            #Se comparan ambos diccionarios con 2 funciones for
            if dicx[x]==dicy[y]:
                #Si hay un elemento en comun, se guarda
                dicf.append(dicx[x])
    return dicf
    #Se retorna el diccionario que almacena todos los elementos en comun

#Funcion para comprobar si un diccionaro tiene un elemento especifico
def comprobar(dicx,compr):
    #Se usa un for para ir por todos los elementos del diccionario
    for x in range(0,len(dicx)):
        #Si el elemento se encuentra, se retorna de forma inmediata
        if df[x]==compr:
            print("%s esta en el resultado"%compr)
            return
    print("%s no esta en el resultado"%compr)
    return
```
La estructura usada para cada ejercicio es esta:

```python
#Se llama la funcion de interseccion, y se guarda su retorno en una lista
df=inter(d1,d2)
#Se imprime el nombre del ejercicio, junto al resultado de la interseccion
print("Primer ejercicio %s"%df)


df=inter(d1,d2)
print("Octavo ejercicio %s"%df)
#En el caso de que el ejercicio necesite comprobacion, se añade de forma extra una llamada a la funcion encargada
comprobar(df,"a")
```


## Concatenacion



## Proceso del Pull Request

Con el fin de colaborar juntos en el trabajo, se envió solicitud de colaboración a todos los entes participantes de la actividad.

## ¿Cómo clonar el repositorio?

1) Abrir el cmd
2) En el cmd, hay que dirigirnos a la carpeta donde se quiere instalar el proyecto, para esto usamos:
 ```bash
cd <dirección_de_la_carpeta>
```
3) Seguido, llamamos el proyecto digitando:
```bash
git clone https://github.com/JuanGuillermoSierraPoveda/UnionInterseccionConcatenacion1234567890
```
## Rama 3
## los comandos usados para los ejercicios

-git checkout -b rama3
- git add lenguajes.py README.MD
lenguajes concatenados (L1, L2)
L1 Y L2 PARAMETROS (LENGUAJES)
estos dos generan un nuevo lenguaje con todas las combianciones posibles x+y donde x pertenecia a L1 y e l2
un ejemplo mas claro de lo que se realizo
## ejemplo:
```
L1 = {"a", "b"}
l2 = {"c","d"}
la union de estos dos seria
{"ac","ad","bc","bd"}
```
# resumen de los 10 ejercicios que se hicieron en la rama 3
1 Concatenación L1 · L3

2 Concatenación L3 · L1

3 Concatenación L4 · L5

4 Concatenación L5 · L4

5 Concatenación L1 · L2

6 Concatenación de lenguajes finitos A={"a","b"}, B={"a","c"}

7 Concatenación de lenguajes finitos A={"0","1"}, B={ε,"00"}

8 Verificación de la palabra "aba" en (L1 · L2)

9 Verificación de la palabra "cab" en (L3 · L4)

10 Ejemplo adicional de prueba con concatenacion_lenguajes

# Concatenacion del lenguaje
estas dos partes del codigo de la rama 3 son las mas importantes ya que son las que realizan la operacion de varios lenguajes L1, L2; L3, L4, L5

```python
def concatenacion_lenguajes(L1, L2):
    resultado = set()
    for x in L1:
        for y in L2:
            resultado.add(x + y)
    return resultado
``` 
concatenacion_lenguajes(L1, L2): recibe dos lenguajes finitos y genera un nuevo lenguaje con todas las combinaciones posibles uniendo cada cadena de L1 con cada cadena de L2.

Ejemplo: L1 = {"a", "b"}, L2 = {"c", "d"} → Resultado: {"ac", "ad", "bc", "bd"}.

```python
def comprobar(L, palabra):
    if palabra in L:
        print(f"La palabra '{palabra}' SÍ pertenece al lenguaje.")
    else:
        print(f"La palabra '{palabra}' NO pertenece al lenguaje.")
```

comprobar(L, palabra): revisa si una palabra específica pertenece al lenguaje resultante e imprime un mensaje indicando si está o no.

Ejemplo: "ad" pertenece, "aa" no pertenece.
