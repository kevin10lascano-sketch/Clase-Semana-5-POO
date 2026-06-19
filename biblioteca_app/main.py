from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca


def main():

    # Importación de clases desde otros módulos
    # para reutilizar código organizado

    # CREACIÓN DE OBJETOS LIBRO

    libro1 = Libro(
        "Python para Principiantes",
        "Juan Pérez",
        "ISBN001",
        250,
        15.99,
        True
    )

    libro2 = Libro(
        "Programación Orientada a Objetos",
        "María Gómez",
        "ISBN002",
        320,
        18.50,
        True
    )


    # CREACIÓN DE OBJETOS USUARIO

    usuario1 = Usuario(
        "Carlos López",
        "carlos@correo.com",
        20,
        True
    )

    usuario2 = Usuario(
        "Ana Torres",
        "ana@correo.com",
        22,
        True
    )


    # Creación de un objeto Biblioteca

    biblioteca = Biblioteca()


    # Registro de objetos en las listas
    # de la biblioteca

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    biblioteca.agregar_usuario(usuario1)
    biblioteca.agregar_usuario(usuario2)


    # Visualización de la información
    # almacenada en las listas

    print("=== LIBROS REGISTRADOS ===")
    biblioteca.mostrar_libros()

    print("\n=== USUARIOS REGISTRADOS ===")
    biblioteca.mostrar_usuarios()


# Punto de inicio del programa

if __name__ == "__main__":
    main()