from django.urls import path
from . import views

urlpatterns = [
    path('equipamentos/cadastro.html', views.cadastro, name='cadastro')
]
