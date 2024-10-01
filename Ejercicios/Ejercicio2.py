#Cree una clase llamada Libro que tenga los siguientes atributos:
#• titulo (str)
#• autor (str)
#• anio_publicacion (int)
#• numero_paginas (int)

#Y un método:
#• mostrar_informacion(): Imprime la información del libro.

class Libro:
    def __init__(self,Titulo,Autor,anio_publicacion,numero_paginas):
        self.Titulo = Titulo
        self.Autor = Autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas
        
    def mostrar_info(self):
        return print(f"El libro {self.Titulo} con Autor {self.Autor} fue publicado \n en {self.anio_publicacion} y tiene {self.numero_paginas} paginas")
        
mi_libro = Libro("Verity: La sombra de un enganio","Colleen Hoover",2018,368)
mi_libro.mostrar_info()