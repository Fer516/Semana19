from django.contrib import admin
from django.urls import path
from appSemana19 import views as ap1v

urlpatterns = [
    path('', ap1v.index, name="home"),
    path('registro/', ap1v.reg_user),
    path('login/', ap1v.iniciar_sesion,name="login"),
    path('logout/', ap1v.cerrar_sesion, name='logout'),
]
