from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=80)
    clave = models.CharField(max_length=60)
    correo = models.CharField(max_length=80)
    numero = models.CharField(max_length=10)
    rol = models.CharField(
        max_length=20,
        choices=[("autor", "Autor"), ("lector", "Lector"), ("admin", "Administrador")],
        default="lector"
    )

    def __str__(self):
        return self.nombre