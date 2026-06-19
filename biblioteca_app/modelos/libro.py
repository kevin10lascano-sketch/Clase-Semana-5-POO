class Libro:

    def __init__(self,
        titulo: str,
        autor: str,
        isbn: str,
        paginas: int,
        precio: float,
        disponible: bool
    ):

        # Identificadores descriptivos para almacenar
        # la información de cada libro

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

        # Tipos de datos numéricos

        self.paginas = paginas
        self.precio = precio

        # Tipo de dato lógico

        self.disponible = disponible

    def mostrar_informacion(self) -> str:

        # Retorna una cadena de texto con la
        # información principal del libro

        return (
            f"Título: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"Páginas: {self.paginas}"
        )

    def __str__(self) -> str:

        # Representación en texto del objeto Libro

        return (
            f"{self.titulo} | "
            f"{self.autor} | "
            f"${self.precio}"
        )