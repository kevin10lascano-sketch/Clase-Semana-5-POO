class Biblioteca:

    def __init__(self):

        # Estructuras de datos compuestas (listas)
        # para almacenar múltiples objetos

        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro) -> None:

        # Agrega un objeto Libro a la lista

        self.libros.append(libro)

    def agregar_usuario(self, usuario) -> None:

        # Agrega un objeto Usuario a la lista

        self.usuarios.append(usuario)

    def mostrar_libros(self) -> None:

        # Recorre la lista de libros y muestra
        # cada objeto almacenado

        for libro in self.libros:
            print(libro)

    def mostrar_usuarios(self) -> None:

        # Recorre la lista de usuarios y muestra
        # cada objeto almacenado

        for usuario in self.usuarios:
            print(usuario)