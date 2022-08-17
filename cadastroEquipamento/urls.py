from django.urls import path
from . import views

urlpatterns = [
    path('retirada/', views.cadastro, name='cadastrar'),
    # path('entrada/', views.entrada, name='entrada'),
]
