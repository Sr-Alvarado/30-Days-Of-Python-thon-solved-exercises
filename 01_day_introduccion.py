# Ejercicio 1: Verificar la versión de Python
import sys # Módulo de la biblioteca estandar de Python.

versionFullData = sys.version # Imprime "3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]"
versionList = versionFullData.split() # Parte un string, dividiendolo por los espacios, y lo trasforma en una lista.
versionNumber = versionList[0] # Pedimos que nos devuelva solo el primer elemento de la lista.

print("1.La versión local de Python es:",versionNumber,"\n")

# Ejecicio 2: Operaciones
## Declaramos las variables
a=4
b=3

sum = a + b
subs = a - b
multi = a * b
modul = a % b
div = a / b
exp = a ** b
floor = a // b

print(f"""2.Operaciones con {a} y {b}: 
    Suma: {sum}
    Resta: {subs}
    Mutiplicación: {multi}
    Módulo: {modul}
    División: {div}
    Potencia: {exp}
    División entera: {floor}
""",)

# Ejercicio 3: Cadenas de texto
## Declarando las variables
name = "Mi nombre"
lastName = "Mi apellido"
country = "Mi pais"
phrase = "Estoy disfrutando de escribir código en python"

print(f"""3.Cadenas de texto:
    Nombre: {name}
    Apellido: {lastName}
    País: {country}
    Comentario: {phrase}
""")

#Ejercicio 4: Tipos de datos
print("4.Verificar el tipo de dato")
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Your name"))
print(type("Your family name"))
print(type("Your country"))
print("")

#5.Definiendo mis datos
intData = 20
floatData = 20.5
complexData = 20j
strData = "hello"
boolData = True
listData = [intData,floatData,complexData,strData,intData,boolData,strData]
tupleData = tuple(listData)
setData = set(tupleData)
dictData = dict([('a', 1), ('b', 2), ('c', 3)]) # Convertimos a diccionario una lista de tuplas de pares.

print(f"""5.Creando mis propios datos
    Entero:          {intData}
    Decimal:         {floatData}
    Complejo:        {complexData}
    Cadena de texto: {strData}
    Boleano:         {boolData}
    Lista:           {listData}
    Tupla:           {tupleData}
    Set:             {setData}
    Diccionario:     {dictData}
""")

# 6. Hallando la distacia euclidiana
## Declarar las variables
firstPoint = [2,3]
LastPoint = [10,8]

## Definir la formula
euclideanDistance=((firstPoint[1]-firstPoint[0])**2+(LastPoint[1]-LastPoint[0])**2)**0.5
print(f"6.La distancia euclidiana entre {tuple(firstPoint)} y {tuple(LastPoint)} es: {euclideanDistance}")
