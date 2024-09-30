import streamlit as st


def saludar(nombre):
    return f"Hola, {nombre}"


def sumar(a, b):
    return a + b


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


def calcular_precio_final(precio_original, descuento=10, impuesto=16):
    precio_con_descuento = precio_original - (precio_original * descuento / 100)
    precio_final = precio_con_descuento + (precio_con_descuento * impuesto / 100)
    return precio_final


def sumar_lista(numeros):
    return sum(numeros)


def producto(nombre_producto, cantidad=1, precio_por_unidad=10):
    return cantidad * precio_por_unidad


def numeros_pares_e_impares(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return pares, impares


def multiplicar_todos(*args):
    if len(args) == 0:
        return 1
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado


def informacion_personal(**kwargs):
    return "\n".join([f"{key}: {value}" for key, value in kwargs.items()])


def calculadora_flexible(num1, num2, operacion="suma"):
    operaciones = {
        "suma": num1 + num2,
        "resta": num1 - num2,
        "multiplicacion": num1 * num2,
        "division": num1 / num2 if num2 != 0 else "Error: División por cero"
    }
    return operaciones.get(operacion, "Operación no válida")

st.title(" Funciones ")

# para seleccionar el ejercicio
ejercicio = st.sidebar.selectbox("Selecciona un ejercicio", list(range(1, 11)))

# Inicializar variable para mostrar resultado
resultado = ""

if ejercicio == 1:
    nombre = st.text_input("Ingresa tu nombre:")
    if st.button("Saludar"):
        resultado = saludar(nombre)

elif ejercicio == 2:
    a = st.number_input("Ingresa el primer número:", 0)
    b = st.number_input("Ingresa el segundo número:", 0)
    if st.button("Sumar"):
        resultado = sumar(a, b)

elif ejercicio == 3:
    base = st.number_input("Ingresa la base del triángulo:", 0.0)
    altura = st.number_input("Ingresa la altura del triángulo:", 0.0)
    if st.button("Calcular área"):
        resultado = calcular_area_triangulo(base, altura)

elif ejercicio == 4:
    precio_original = st.number_input("Ingresa el precio original:", 0.0)
    descuento = st.number_input("Ingresa el descuento (%):", 10.0)
    impuesto = st.number_input("Ingresa el impuesto (%):", 16.0)
    if st.button("Calcular precio final"):
        resultado = calcular_precio_final(precio_original, descuento, impuesto)

elif ejercicio == 5:
    numeros = st.text_input("Ingresa una lista de números separados por comas:")
    if st.button("Sumar lista"):
        try:
            lista_numeros = list(map(float, numeros.split(',')))
            resultado = sumar_lista(lista_numeros)
        except ValueError:
            resultado = "Por favor, ingresa solo números válidos."

elif ejercicio == 6:
    nombre_producto = st.text_input("Nombre del producto:")
    cantidad = st.number_input("Cantidad:", 1, min_value=1)
    precio_por_unidad = st.number_input("Precio por unidad:", 10.0)
    if st.button("Calcular total"):
        resultado = producto(nombre_producto, cantidad, precio_por_unidad)

elif ejercicio == 7:
    numeros = st.text_input("Ingresa una lista de números separados por comas:")
    if st.button("Separar pares e impares"):
        try:
            lista_numeros = list(map(int, numeros.split(',')))
            pares, impares = numeros_pares_e_impares(lista_numeros)
            resultado = f"Números pares: {pares}\nNúmeros impares: {impares}"
        except ValueError:
            resultado = "Por favor, ingresa solo números válidos."

elif ejercicio == 8:
    numeros = st.text_input("Ingresa números separados por comas:")
    if st.button("Multiplicar todos"):
        try:
            lista_numeros = list(map(float, numeros.split(',')))
            resultado = multiplicar_todos(*lista_numeros)
        except ValueError:
            resultado = "Por favor, ingresa solo números válidos."

elif ejercicio == 9:
    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad:", 0)
    direccion = st.text_input("Dirección:")
    if st.button("Mostrar información"):
        resultado = informacion_personal(nombre=nombre, edad=edad, direccion=direccion)

elif ejercicio == 10:
    num1 = st.number_input("Ingresa el primer número:", 0.0)
    num2 = st.number_input("Ingresa el segundo número:", 0.0)
    operacion = st.selectbox("Selecciona una operación:", ["suma", "resta", "multiplicacion", "division"])
    if st.button("Calcular"):
        resultado = calculadora_flexible(num1, num2, operacion)

# Mostrar el resultado en pantalla
if resultado:
    st.write(f"**Resultado:** {resultado}")
