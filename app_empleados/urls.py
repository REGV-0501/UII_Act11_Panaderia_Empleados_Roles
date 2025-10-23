from django.urls import path
from . import views

app_name = 'app_empleados'

urlpatterns = [
    path('', views.listar_empleados, name='listar_empleados'),
    path('empleado/<int:empleado_id>/', views.detalle_empleado, name='detalle_empleado'),
    path('empleado/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleado/editar/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('empleado/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),
]