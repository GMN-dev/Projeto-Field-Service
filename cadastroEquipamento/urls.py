from django.urls import path
from . import views

urlpatterns = [
    path('equipamentos/', views.cadastro, name='cadastro_url')
]
