from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.

#----------------------------------------------------------------------------------------------------------------
#TABLA USUARIO

class Usuario(models.Model):
    IdUsuario = models.AutoField(primary_key=True)  # ID auto-incrementable
    Nombre = models.CharField(max_length=80)  # Nombre completo del usuario
    Cuenta = models.EmailField(unique=True)  # Campo para el correo electrónico, único y validado
    Contrasena = models.CharField(max_length=128)  # Contraseña encriptada (gestionada por Django)
    
    # Opciones de rol del usuario
    ROL_CHOICES = [
        ('mesero', 'Mesero'),
        ('chef', 'Chef'),
    ]
    Rol = models.CharField(max_length=10, choices=ROL_CHOICES)  # Rol del usuario (mesero o chef)


    def __str__(self):
        usuario_detalle = "({0}) {1} {2}"
        return usuario_detalle.format(self.IdUsuario, self.Nombre, self.Rol)
    
#---------------------------------------------------------------------------------------------------------------
#TABLA PEDIDO

class Pedido(models.Model):
    IdPedido = models.AutoField(primary_key=True)  # ID auto-incrementable para cada pedido
    Mesa = models.IntegerField()  # Número de la mesa
    Platillo = models.CharField(max_length=100)  # Descripción del platillo

    # Estatus del pedido
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
    ]

    Estatus = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente') #Estatus pendiente por default

    UsuarioRegistro = models.ForeignKey(Usuario, on_delete=models.CASCADE)  #Usuario que registro el pedido
    FechaRegistro = models.DateTimeField(auto_now_add=True)  #Fecha del registro automaticamente

    @property
    def FechaFormateada(self):
        return self.FechaRegistro.strftime('%d/%m/%Y')
    
    def __str__(self):
        return f"Pedido {self.IdPedido} - Mesa: {self.Mesa} - Platillo: {self.Platillo} - Estatus: {self.Estatus} - Usuario a cargo: {self.UsuarioRegistro.Nombre} - Fecha :{self.FechaFormateada}"
