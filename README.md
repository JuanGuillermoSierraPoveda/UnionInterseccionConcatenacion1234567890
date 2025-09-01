# Resumen del trabajo

## Union

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