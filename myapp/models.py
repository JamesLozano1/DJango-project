from django.db import models

class Project( models.Model ):
    '''
    Modelo que representa un proyecto
    '''
    name = models.CharField(max_length=50, help_text='Ingrese el nombre del projecto')

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200, help_text='Ingrese el título de la tarea')
    description = models.CharField(max_length=200, help_text='Ingrese la descripción de la tarea')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # def __str__(self):
        # return self.title + ' - ' + str(self.project.name)

    def __str__(self) -> str:
        return self.title + ' - ' + self.project.name

#CharField:  Almacena una cadena de caracteres de longitud limitada.

# class persona(models.Model):
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)

# #IntegerField: Almacena un número entero.

# class Producto(models.Model):
#     codigo = models.IntegerField()
#     cantidad_disponible = models.IntegerField()

# #DateField: Almacena una fecha.

# class Evento(models.Model):
#     nombre = models.CharField(max_length=200)
#     fecha_inicio = models.DateField()

# #BooleanField: Almacena un valor booleano (True o False).

# class Tarea(models.Model):
#     descripcion = models.CharField(max_length=200)
#     completada = models.BooleanField(default=False)

# #ForeignKey: Establece una relación de clave externa entre dos modelos.

# class Autor(models.Model):
#     nombre = models.CharField(max_length=100)

# class Libro(models.Model):
#     titulo = models.CharField(max_length=200)
#     autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


# #ManyToManyField: Establece una relación de muchos a muchos entre dos modelos.

# class Etiqueta(models.Model):
#     nombre = models.CharField(max_length=50)

# class Articulo(models.Model):
#     titulo = models.CharField(max_length=200)
#     etiquetas = models.ManyToManyField(Etiqueta)

# #ImageField: Almacena una imagen.

# class Perfil(models.Model):
#     nombre = models.CharField(max_length=100)
#     foto = models.ImageField(upload_to='perfiles/')

# #TextField: Almacena texto largo.

# class Publicacion(models.Model):
#     titulo = models.CharField(max_length=200)
#     contenido = models.TextField()

# #DateTimeField: Almacena fecha y hora.

# class Evento(models.Model):
#     nombre = models.CharField(max_length=200)
#     fecha_hora = models.DateTimeField()

# #URLField: Almacena una URL.

# class Pagina(models.Model):
#     titulo = models.CharField(max_length=200)
#     url = models.URLField()
