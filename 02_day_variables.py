# Level 1
first_name = "Primer"
last_name = "Nombre"
full_name = first_name + " " + last_name
country = "Pais"
city = "Ciudad"
age = "123"
year = "1900"
is_married = True
is_true = False
is_light_on = True
var1, var2, var3, var4 = True, 2.0, "tres", 4

# Level 2
## Ejer 1
### !Puedo usar una función para extraer el nombre, valor y tipo de una variable, luego usar JOIN para hacer saltos de página.
print("\n",
    first_name, type(first_name), "\n",
    last_name, type(last_name), "\n",
    full_name, type(full_name), "\n",
    country, type(country), "\n",
    city, type(city), "\n",
    age, type(age), "\n",
    year, type(year), "\n",
    is_married, type(is_married)
)

## Ejer 2
longitud_nombre = len(first_name)
print("La longitud de mi nombre es:",longitud_nombre)

## Ejer 3
longitud_apellido = len(last_name)
print("Nombre:",longitud_nombre,"\n", "Apellido",longitud_apellido)

## Ejer 4
num_one = 5
num_two = 4
total = num_one + num_two       ### i
diff = num_one - num_two        ### ii
product = num_one * num_two     ### iii
division = num_one / num_two    ### iv
mod = num_one % num_two
remainder = num_one + mod       ### v
exp = num_one ** num_two        ### vi
floor_divition = division - mod ### vii

## Ejer 5
radius = 30
pi = 355 / 113

### area
area_of_circle = pi * (radius ** 2)

### circumference
circum_of_circle = pi * (radius * 2)

### input radius
radius_input = int(input("Ingrese un valor para el radio: "))
area_input = pi * (radius_input ** 2)
print(area_input)

## Ejer 6
user_first_name = input("Ingrese su nombre: ")
user_last_name = input("Ingrese su apellido: ")
user_country = input("Ingrese su pais: ")
user_age = input("Ingrese su edad: ")
print(f"""
Nombre: {user_first_name}
Apellido: {user_last_name}
País: {user_country}
Edad: {user_age}
""")