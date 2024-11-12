from django.shortcuts import render, redirect
from .models import Usuario, Pedido
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Vista de home (login)
def home(request):
    return render(request, "login.html")

# Vista de pantallaMesero
def pantallaMesero(request):
    lstPedido = Pedido.objects.all()  # Trae todos los datos de la tabla Pedido
    lstUsuario = Usuario.objects.all()  # Trae todos los datos de la tabla Usuario
    lstUsuariosMeseros = Usuario.objects.filter(Rol='mesero')  # Trae los usuarios con rol de mesero

    return render(request, "pantallaMesero.html", {"tblPedido": lstPedido, "tblUsuario": lstUsuario, "tblUsuariosMeseros": lstUsuariosMeseros})

# Vista de pantallaChef
def pantallaChef(request):
    lstPedido = Pedido.objects.all()
    return render(request, "pantallaChef.html", {"tblPedido": lstPedido})

# Vista de registro
def registro(request):
    return render(request, "registro.html")

# Vista para registrar un nuevo usuario
def registrarUsuario(request):
    pNombre = request.POST["txtNombre"]
    pCuenta = request.POST["txtCuenta"]
    pContrasena = request.POST["txtContrasena"]
    pRol = request.POST["ddlRol"]
    
    Usuario.objects.create(
        Nombre=pNombre,
        Cuenta=pCuenta,
        Contrasena=pContrasena,
        Rol=pRol
    )
    return redirect("/")  # Redirigir a la página principal después de registrar un usuario

# Vista de login
def redireccion(request):
    if request.method == 'POST':
        cuenta = request.POST['txtCuenta']  # El correo del usuario
        contrasena = request.POST['txtContrasena']  # La contraseña ingresada por el usuario
        
        try:
            # Buscar al usuario por su cuenta (correo electrónico)
            usuario = Usuario.objects.get(Cuenta=cuenta)
            
            # Verificar si la contraseña ingresada coincide
            if usuario.Contrasena == contrasena:
                # Aquí no necesitas usar login(request, usuario) porque no estás usando el modelo User de Django
                
                # Guardar el rol del usuario en la sesión
                request.session['usuario_rol'] = usuario.Rol.lower()  # Guardar rol en la sesión
                
                rol_usuario = usuario.Rol.lower()  # Obtener el rol del usuario (chef o mesero)
                
                # Redirigir dependiendo del rol
                if rol_usuario == 'chef':
                    return redirect('pantallaChef')  # Redirige a la pantalla del chef
                elif rol_usuario == 'mesero':
                    return redirect('pantallaMesero')  # Redirige a la pantalla del mesero
                else:
                    return redirect('/')  # Redirige a la página principal si no es ni chef ni mesero
                
            else:
                messages.error(request, "Contraseña incorrecta.")
                return redirect('redireccion')  # Si la contraseña no es correcta, vuelve al login
        except Usuario.DoesNotExist:
            messages.error(request, "No se encontró un usuario con esa cuenta.")
            return redirect('redireccion')  # Si no se encuentra el usuario, vuelve al login

    return render(request, 'login.html')  # Si es un GET, muestra el formulario de login



# Vista para registrar pedidos
def registrarPedido(request):
    # Si es un POST, procesar el registro del pedido
    if request.method == 'POST':
        pUsuarioRegistro = request.POST.get('ddlUsuarioRegistro')  # ID del mesero seleccionado
        pMesa = request.POST.get("txtMesa")
        pPlatillo = request.POST.get("txtPlatillo")
        
        # Obtener el objeto Usuario usando el ID
        usuario_registro = Usuario.objects.get(IdUsuario=pUsuarioRegistro)

        # Crear un nuevo pedido asociando correctamente el objeto Usuario
        Pedido.objects.create(
            Mesa=pMesa,
            Platillo=pPlatillo,
            UsuarioRegistro=usuario_registro  # Asociar el objeto Usuario completo
        )
        
        # Redirigir a la pantalla del mesero después de registrar el pedido
        return redirect('pantallaMesero')

    # Si no es un POST, mostrar el formulario de pedido
    return render(request, "pantallaMesero")


#--------------------------------------------------------------------------------------------------------------
#redireccion a pantalla de mesero

def ver_pedidos_mesero(request):
    if 'usuario_rol' in request.session:
        usuario_rol = request.session['usuario_rol']
        
        request.session['usuario_id'] = request.user.id  # Guarda el ID en la sesión
        
        if usuario_rol == 'mesero':
            return render(request, 'pantallaMesero.html')
        else:
            return redirect('login')
    else:
        return redirect('login')


  
#redireccion a pantalla chef

def ver_pedidos_chef(request):
    #verificar si el usuario tiene sesion activa
    if 'usuario_rol' in request.session:
        usuario_rol = request.session['usuario_rol']
        
        #verificar si el rol es chef
        if usuario_rol == 'chef':
            return render(request, 'pantallaChef.html')
        #Si el rol no es chef, redirigir al login
        else:
            return redirect('login')
    #Si no hay sesion activa redirigir al login
    else:
        return redirect('login')
    
#----------------------------------------------------------------------------------------------------------------------------------

#Acciones de pedido

def editarPedido(request, pIdPedido):
    pedido = Pedido.objects.get(IdPedido=pIdPedido)
    return render(request, "editPedido.html", {"tblPedido": pedido})

def eliminarPedido(request, pIdPedido):
    pedido = get_object_or_404(Pedido, IdPedido=pIdPedido)
    pedido.delete()
    return redirect("pantallaMesero") 

def leerPedido(request):
    pMesa = request.POST["txtMesa"]
    pPlatillo = request.POST["txtPlatillo"]
    pUsuarioRegistro = request.POST.get('ddlUsuarioRegistro')
    
def aceptarPedido(request, pIdPedido):
    pedido=Pedido.objects.get(IdPedido=pIdPedido)
    pedido.Estatus = "aceptado"
    pedido.save()
    return redirect("/ver_pedidos_chef")
#------------------------------------------------------------------------------------------------------------------------------------

#Acciones de usuario

def eliminarUsuario(request):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        usuario = request.user  # Obtener el usuario autenticado

        # Eliminar al usuario
        usuario.delete()

        # Redirigir al login
        return redirect('login')
    else:
        # Si el usuario no está autenticado, redirigir a la página de login
        return redirect('login')
