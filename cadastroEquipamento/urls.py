from django.urls import path, include
from . import views
from .api.views import DashboardView, TblSolicitacaoView
from rest_framework import routers


route = routers.DefaultRouter()
route.register(r'incidentes', TblSolicitacaoView, basename="api-retirada")
route.register(r'dashboard', DashboardView, basename="api-dashboard")

urlpatterns = [
    path('dashboard/', views.dashboard_incidentes, name='dashboard'),
    path('incidente/<slug:chamado>', views.incidente_details, name='incidente_details'),
    path("deletar/incidente/<int:id_solicitacao>", views.excluirSolicitacao, name="deletar"),
    path('operacoes/', views.operacoesAtivas, name="operacoesAtivas"),
    path('operacoes/<str:operacao>/<int:pk>', views.operacao_details, name="operacao_details"),
    path('operacoes/deletar/<str:operacao>', views.excluirOperacao, name="excluirOperacao"),
    path('api/', include(route.urls))  
    # path('entrada/', views.entrada, name='entrada'),
] 

  