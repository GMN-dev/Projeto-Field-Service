from django.urls import path, include
from . import views
from .api.views import SolicitacaoView
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'dashboard', SolicitacaoView, basename="api-retirada")


urlpatterns = [
    path('dashboard/', views.cadastro, name='cadastrar'),
    path("deletar/incidente/<int:id_solicitacao>", views.excluirSolicitacao, name="deletar"),
    path('api/', include(route.urls)) 
    # path('entrada/', views.entrada, name='entrada'),
] 

