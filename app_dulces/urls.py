from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_dulceria, name='inicio_dulceria'),
    path('agregar_dulce/', views.agregar_dulce, name='agregar_dulce'),
    path('ver_dulces/', views.ver_dulces, name='ver_dulces'),
    path('actualizar_dulce/<int:id>/', views.actualizar_dulce, name='actualizar_dulce'),
    path('realizar_actualizacion_dulce/<int:id>/', views.realizar_actualizacion_dulce, name='realizar_actualizacion_dulce'),
    path('borrar_dulce/<int:id>/', views.borrar_dulce, name='borrar_dulce'),
    path('realizar_borrado_dulce/<int:id>/', views.realizar_borrado_dulce, name='realizar_borrado_dulce'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('ver_clientes/', views.ver_clientes, name='ver_clientes'),
    path('actualizar_cliente/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('realizar_actualizacion_cliente/<int:id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('borrar_cliente/<int:id>/', views.borrar_cliente, name='borrar_cliente'),
    path('realizar_borrado_cliente/<int:id>/', views.realizar_borrado_cliente, name='realizar_borrado_cliente'),
]
