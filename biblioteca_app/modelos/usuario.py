class Usuario:

    def __init__(
        self,
        nombre: str,
        correo: str,
        edad: int,
        activo: bool
    ):

        # Identificadores descriptivos para almacenar
        # la información de cada usuario

        self.nombre = nombre
        self.correo = correo

        # Tipo de dato numérico entero

        self.edad = edad

        # Tipo de dato lógico

        self.activo = activo

    def mostrar_informacion(self) -> str:

        # Retorna una cadena de texto con la
        # información principal del usuario

        return (
            f"{self.nombre} | "
            f"{self.correo}"
        )

    def __str__(self) -> str:

        # Representación en texto del objeto Usuario

        return (
            f"{self.nombre} "
            f"({self.edad} años)"
        )