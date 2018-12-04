from django.urls import path

from . import views

urlpatterns = [
    #path('calcular/<int:num_uno>/<int:num_dos>', views.calcular, name='calcular'),
	path('', views.index, name='index'),
	path('gracias/', views.gracias, name='gracias'),
]