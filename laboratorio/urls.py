from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path('mostrar/', views.mostrar_laboratorio_view, name='mostrar_laboratorio'),
    path('insertar/', views.insert_view, name='insertar_laboratorio'),
    path('complete/', views.insertar_laboratorio_view, name='complete'),
    path('eliminar/<int:pk>/', views.eliminar_laboratorio_view, name='eliminar_lab'),
    path('update/<int:pk>/', views.update_view, name='update'),
    path('updatelab/<int:pk>/', views.editar_laboratorio_view, name='updatelab'),
]
