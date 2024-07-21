# Ejer 1
age = 99

# Ejer 2
height = 3.3

# Ejer 3
complex_number = 5

# Ejer 4. Área triangulo
print("""1. Calc area of triangle
==================================""")
base = int(input("   Enter base: "))
altura = int(input("   Enter height: "))

area = base * altura * 0.5
print(f"""----------------------------------
The area of the triangle is {area:.2f}\n""")

# Ejer 5. Perímetro triangulo
print("""2. Calc perimeter of triangle
==================================""")
side_a = int(input("   Enter side a of triangle: "))
side_b = int(input("   Enter side b of triangle: "))
side_c = int(input("   Enter side c of triangle: "))

tri_perimeter = side_a + side_b + side_c
print(f"""----------------------------------
The perimeter of the triangle is {tri_perimeter:.2f}\n""")

# Ejer 6. Area and perimetrer of rectangle
print("""3. Calc area and perimeter of rectangle
==================================""")
length = int(input("   Enter length of the rectangle: "))
width = int(input("   Enter width of the rectangle: "))

rect_perimeter = (length + width) * 2
rect_area = length * width

print(f"""----------------------------------
The perimeter of the rectangle is {rect_perimeter:.2f} and
the area of the rectangle is {rect_area:.2f}\n""")

# Ejer 7. Area and circumference of circle
print("""4. Calc area and circumference of circle
==================================""")
radio = int(input(f"   Enter radio of circle: "))
pi = 355 / 113

cir_area = pi * (radio ** 2)
cir_curcumference = 2 * pi * radio

print(f"""----------------------------------
The area of the circle is {cir_area:.2f} and
the circumference of the circle is {cir_curcumference:.2f}
""")

# Ejer 8. Find the slope

def form_y(x):
    y_value = (2 * x) - 2
    return y_value

x_values = [0,1]    
y_values = [form_y(x) for x in x_values]

def form_change(x,y):
    return x-y

change = [form_change(x,y) for x, y in zip(x_values, y_values)]

form_slope = change[0] / change[1]

print(f"""5. Encontrar la pendiente y las intersecciones en x,y para y=2x-2
==================================
La pendiente (m) para y=2x-2 es: {form_slope}
Cuando x es 0 y={tuple(y_values)}
Cuando y es 0 x={tuple(x_values)}
""")

# Ejer 9. Encuentra la y la distancia Euclidiana.
point_1 = [3,2]
point_2 = [6,10]

slope = (point_2[1]-point_2[0])/(point_1[1]-point_1[0])
euclidian_distance = (((point_1[0]-point_2[0])**2)+((point_1[1]-point_2[1])**2))**0.5

print(f"""La pendiente es: {slope}
La distancia euclidiana es: {euclidian_distance}""")

# Ejer 10. Comparar las pendientes del ejer 8 y 9

print(f"""
La pendiente para Y=2x-2 es: {form_slope}
La pendiente para x(3,2) y Y(6,10) es: {slope}
""")

# Ejer 11. Hallar X para y = x^2 + 6x + 9
x_val = list(range(9))

def y_form(x):
    form = x**2 + 6*x + 9
    return form

y_val = [y_form(x) for x in x_val]

for x,y in zip(x_val,y_val):
    print(f"Cuando X es {x} Y es {y}")

# Ejer 12. Encontrar la longitud de "python" y "dragon", y compararlos
value_one = "python"
value_two = "dragon"

length_one = len(value_one)
length_two = len(value_two)

if length_one > length_two:
    print(f"{value_one} con {length_one} caracteres es más grande que {value_two} con {length_two} caracteres")
elif length_two > length_one:
    print(f"{value_two} con {length_two} caracteres es más grande que {value_one} con {length_one} caracteres")
else:
    print(f"{value_one} y {value_two} tienen la misma longitud con {length_one} caracteres")

# Ejer 13. Verifica si "on" es parte de "python" y de "dragon"
"on" in ("python" and "dragon")

# Ejer 14. Verifica si "jargon" está dentro de "I hope this course is not full of jargon"
"jargon" in "I hope this course is not full of jargon"

# Ejer 15. Verifica que "on" no es parte de "python" y de "dragon"
"on" not in ("python" and "dragon")

# Ejer 16. Halla la longitud de "python", vuelvela un flotante y luego string
longitud = len("python")
longitud_float = float(longitud)
longitud_string = str(longitud_float)

print(longitud_float,longitud_string)

# Ejer 17. Identifica los números pares
numero = int(input("Escribe un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")

# Ejer 18.
7 % 3 == int(2.7)

# Ejer 19. 
print(type("10") == type(10))

# Ejer 20.
print(int(float("9.8")) == 10)

# Ejer 21.
hour_user = int(input("Enter hours: "))
rate_user = int(input("Enter per hour: "))

pay = hour_user*rate_user

print(f"Your weekly earning is {pay}")

# Ejer 22.
years_user = int(input("Enter your age: "))

seconds_live = years_user * 365 * 24 * 60 * 60

print(f"You have lived for {seconds_live} seconds")

# Ejer 23. Imprimir
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1, 6):
    for j in [1] + list(range(4)):
        print(i ** (j), end=" ") # La función end indica que al final del resultado agregará un espacio " "
    print()