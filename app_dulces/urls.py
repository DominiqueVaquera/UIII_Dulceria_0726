from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_dulceria, name='inicio_dulceria'),
    path('agregar_dulce/', views.agregar_dulce, name='agregar_dulce'),
    path('ver_dulces/', views.ver_dulces, name='ver_dulces'),
    path('actualizar_dulce/<int:id>/', views.actualizar_dulce, name='actualizar_dulce'),
    path('realizar_actualizacion_dulce/<int:id>/', views.realizar_actualizacion_dulce, name='realizar_actualizacion_dulce'),
    path('borrar_dulce/<int:id>/', views.borrar_dulce, name='borrar_dulce'),
]