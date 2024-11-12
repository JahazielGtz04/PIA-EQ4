from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="login"),
    path('redireccion/', views.redireccion, name='redireccion'),  
    path('registro/', views.registro, name='registro'),
    path("registrarUsuario/", views.registrarUsuario, name='registrarUsuario'),
    path('pantallaMesero/', views.pantallaMesero, name='pantallaMesero'),
    path('pantallaChef/', views.pantallaChef, name='pantallaChef'),
    path("registrarPedido/", views.registrarPedido, name='registrarPedido'),
    path('ver_pedidos_mesero/', views.ver_pedidos_mesero, name='ver_pedidos_mesero'),
    path('ver_pedidos_chef/', views.ver_pedidos_chef, name='ver_pedidos_chef'),
    path("editarPedido/<pIdPedido>", views.editarPedido, name='editarPedido'),
    path("eliminarPedido/<int:pIdPedido>/", views.eliminarPedido, name='eliminarPedido'),
    path("leerPedido", views.leerPedido, name="leerPedido"),
    path('eliminarUsuario/', views.eliminarUsuario, name='eliminarUsuario'),
    path("aceptarpedido/<pIdPedido>", views.aceptarPedido, name='aceptarPedido'),
]