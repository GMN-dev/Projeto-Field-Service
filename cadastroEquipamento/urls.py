from django.urls import path, include

from cadastroEquipamento.api.serializers import DashboardSerializer
from . import views
from .api.views import DashboardView, TblSolicitacaoView
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'dashboard', TblSolicitacaoView, basename="api-retirada")
route.register(r'graph', DashboardView, basename="api-dashboard")

urlpatterns = [
    path('dashboard/', views.cadastro, name='cadastrar'),
    path("deletar/incidente/<int:id_solicitacao>", views.excluirSolicitacao, name="deletar"),
    path('api/', include(route.urls)) 
    # path('entrada/', views.entrada, name='entrada'),
] 

