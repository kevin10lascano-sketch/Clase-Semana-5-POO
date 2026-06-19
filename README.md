# Sistema de Gestión de Biblioteca

## Descripción

Este proyecto consiste en una aplicación básica desarrollada en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar libros y usuarios dentro de una biblioteca, almacenando la información mediante objetos y organizando el código en diferentes módulos para facilitar su comprensión y mantenimiento.

## Estructura del Proyecto

```text
biblioteca_app/
│
├── modelos/
│   ├── libro.py
│   └── usuario.py
│
├── servicios/
│   └── biblioteca.py
│
└── main.py
```

## Funcionalidades

- Crear objetos de tipo Libro.
- Crear objetos de tipo Usuario.
- Registrar libros en la biblioteca.
- Registrar usuarios en la biblioteca.
- Mostrar la información almacenada.
- Organizar el programa mediante módulos y clases.

## Conceptos Aplicados

### Identificadores Descriptivos

Se utilizan nombres claros y significativos para clases, métodos, atributos y variables, facilitando la lectura y comprensión del código.

**Ejemplos:**

- `Libro`
- `Usuario`
- `Biblioteca`
- `titulo`
- `autor`
- `agregar_libro()`
- `mostrar_informacion()`

### Tipos de Datos

Durante el desarrollo del programa se utilizan diferentes tipos de datos:

| Tipo | Ejemplo |
|--------|----------|
| `str` | titulo, autor, correo |
| `int` | paginas, edad |
| `float` | precio |
| `bool` | disponible, activo |

### Anotaciones de Tipos

Se emplean anotaciones de tipos para indicar el tipo de dato esperado en parámetros y valores de retorno.

```python
titulo: str
edad: int
precio: float
```

```python
def mostrar_informacion(self) -> str:
```

### Estructuras de Datos Compuestas

La clase `Biblioteca` utiliza listas para almacenar múltiples objetos.

```python
self.libros = []
self.usuarios = []
```

Estas estructuras permiten registrar varios libros y usuarios dentro del sistema.

### Programación Orientada a Objetos

El proyecto aplica conceptos fundamentales de POO:

- Clases
- Objetos
- Atributos
- Métodos
- Modularidad

## Buenas Prácticas Aplicadas

- Uso de identificadores descriptivos.
- Organización del código en módulos.
- Separación de responsabilidades mediante clases.
- Uso de anotaciones de tipos.
- Comentarios claros para facilitar el aprendizaje.
- Función principal `main()` como punto de entrada del programa.
