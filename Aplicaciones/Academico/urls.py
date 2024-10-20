#Gestiona las rutas solo de academico
from django.urls import path
from . import views #importante

urlpatterns = [
    path('', views.home), #accedemos al diretorio raiza y nos dirigimos a una vista
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>',views.eliminarCurso)
]


