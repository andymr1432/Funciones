# Funciones
Funciones en streamlit
Claro, aquí tienes una explicación detallada del código que se ha proporcionado:

### Explicación del Código

Este código crea una aplicación web utilizando **Streamlit**, que permite a los usuarios interactuar con diversas funciones de Python a través de una interfaz gráfica. A continuación, se desglosa cada sección del código:

####  Importación de Librerías
```python
import streamlit as st
```
Se importa la biblioteca `streamlit`, que es esencial para crear aplicaciones web interactivas en Python.

####  Definición de Funciones
Se definen varias funciones que realizan tareas específicas:

- **Saludo Simple**
  ```python
  def saludar(nombre):
      return f"Hola, {nombre}"
  ```

- **Suma de Dos Números**
  ```python
  def sumar(a, b):
      return a + b
  ```

- **Cálculo del Área de un Triángulo**
  ```python
  def calcular_area_triangulo(base, altura):
      return (base * altura) / 2
  ```

- **Calculadora de Descuento**
  ```python
  def calcular_precio_final(precio_original, descuento=10, impuesto=16):
      ...
  ```

- **Suma de una Lista de Números**
  ```python
  def sumar_lista(numeros):
      return sum(numeros)
  ```

- **Función con Valores Predeterminados**
  ```python
  def producto(nombre_producto, cantidad=1, precio_por_unidad=10):
      return cantidad * precio_por_unidad
  ```

- **Separación de Números Pares e Impares**
  ```python
  def numeros_pares_e_impares(numeros):
      ...
  ```

- **Multiplicación con *args**
  ```python
  def multiplicar_todos(*args):
      ...
  ```

- **Información Personal con **kwargs**
  ```python
  def informacion_personal(**kwargs):
      ...
  ```

- **Calculadora Flexible**
  ```python
  def calculadora_flexible(num1, num2, operacion="suma"):
      ...
  ```

Cada función realiza una tarea específica relacionada con los ejercicios que se proponen.

#### Interfaz de Usuario
```python
st.title("Ejercicios de Funciones en Python")
```
Se establece el título de la aplicación.

####  Selección de Ejercicio
```python
ejercicio = st.sidebar.selectbox("Selecciona un ejercicio", list(range(1, 11)))
```
Se crea un menú en la barra lateral donde el usuario puede seleccionar entre los 10 ejercicios.

####  Lógica para Cada Ejercicio
Se utilizan condicionales (`if-elif`) para determinar cuál ejercicio se debe ejecutar, dependiendo de la selección del usuario. Cada bloque incluye:

- **Entrada de Datos**: Se utilizan diferentes widgets de Streamlit (como `st.text_input`, `st.number_input`, etc.) para obtener los datos necesarios.
  
- **Botones de Acción**: Al presionar un botón, se ejecuta la función correspondiente y se almacena el resultado.

```python
if ejercicio == 1:
    ...
elif ejercicio == 2:
    ...
```

####  Mostrar Resultados
Al final de cada bloque condicional, se utiliza `st.write` para mostrar el resultado en la pantalla, facilitando al usuario ver la salida de la función ejecutada:

```python
if resultado:
    st.write(f"**Resultado:** {resultado}")
```

#### Resumen
Este código proporciona una interfaz sencilla y efectiva para interactuar con diversas funciones en Python. Los usuarios pueden ingresar datos y ver los resultados en tiempo real, lo que es útil tanto para aprender como para practicar habilidades de programación. Además, el uso de Streamlit hace que la aplicación sea accesible y fácil de usar.
