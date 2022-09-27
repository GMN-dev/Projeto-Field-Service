from django.urls import path, include
from . import views
from .api.views import DashboardView, TblSolicitacaoView
from rest_framework import routers


route = routers.DefaultRouter()
route.register(r'incidentes', TblSolicitacaoView, basename="api-retirada")
route.register(r'dashboard', DashboardView, basename="api-dashboard")

urlpatterns = [
    path('dashboard/', views.cadastro, name='dashboard'),
    path('incidente/<slug:chamado>', views.incidente_details, name='incidente_details'),
    path("deletar/incidente/<int:id_solicitacao>", views.excluirSolicitacao, name="deletar"),
    path('dashboard/configuracao', views.configurarDashboard, name="configurarDashboard"),
    path('api/', include(route.urls)) 
    # path('entrada/', views.entrada, name='entrada'),s
] 

