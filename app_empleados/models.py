from django.db import models

class Rol(models.Model):
    # id_rol se crea automáticamente por Django como 'id'
    nombre_rol = models.CharField(max_length=100, unique=True)
    descripcion_rol = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_rol

    class Meta:
        verbose_name = "Rol de Empleado"
        verbose_name_plural = "Roles de Empleados"

class Empleado(models.Model):
    # id_empleado se crea automáticamente por Django como 'id'
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_contratacion = models.DateField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, related_name='empleados', blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_empleados/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['apellido', 'nombre'] # Ordenar por apellido y luego nombre