"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('estudiante/<int:id>', views.obtener_estudiante,
            name='obtener_estudiante'),
        path('crear/estudiante', views.crear_estudiante,
            name='crear_estudiante'),
        path('editar/estudiante/<int:id>', views.editar_estudiante,
            name='editar_estudiante'),
        path('eliminar/estudiante/<int:id>', views.eliminar_estudiante,
            name='eliminar_estudiante'),
        path('agregar/pais', views.agregar_pais,
            name='agregar_pais'),
        path('paises/listado', views.listado_paises,
            name='listado_paises'),
            
 ]
