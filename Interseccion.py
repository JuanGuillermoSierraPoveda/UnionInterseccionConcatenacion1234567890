def inter(dicx,dicy):
    dicf=[]
    print("\nLenguajes a unir\n%s\n%s"%(dicx,dicy))
    for x in range(0,len(dicx)):
        for y in range(0,len(dicy)):
            if dicx[x]==dicy[y]:
                dicf.append(dicx[x])
    return dicf
def comprobar(dicx,compr):
    for x in range(0,len(dicx)):
        if df[x]==compr:
            print("%s esta en el resultado"%compr)
            return
    print("%s no esta en el resultado"%compr)
    return





d1=["a","b","ab","ba"]
d2=["b","c","bc","cb"]
d3=["a", "b", "c"]
d4=["ab", "ac"]
d5=["b","bc","ca","c"]

df=inter(d1,d2)
print("Primer ejercicio %s"%df)
df=inter(d1,d3)
print("Segundo ejercicio %s"%df)
df=inter(d2,d3)
print("Tercer ejercicio %s"%df)
df=inter(d4,d5)
print("Cuarto ejercicio %s"%df)
df=inter(d1,d2)
df=inter(df,d3)
print("Quinto ejercicio %s"%df)

A=["01","10","11"]
B=["10","00","1"]
df=inter(A,B)
print("Sexto ejercicio %s"%df)

A=["x","y","z"]
B=["m","n","z"]
df=inter(A,B)
print("Septimo ejercicio %s"%df)


df=inter(d1,d2)
print("Octavo ejercicio %s"%df)
comprobar(df,"a")

df=inter(d4,d5)
print("Noveno ejercicio %s"%df)
comprobar(df,"b")

df=inter(d1,d5)
print("Decimo ejercicio %s"%df)