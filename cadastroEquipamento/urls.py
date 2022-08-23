from django.urls import path, include
from . import views
from .api.views import SolicitacaoView
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'retirada', SolicitacaoView, basename="api-retirada")


urlpatterns = [
    path('retirada/', views.cadastro, name='cadastrar'),
    path('api/', include(route.urls)) 
    # path('entrada/', views.entrada, name='entrada'),
] 

