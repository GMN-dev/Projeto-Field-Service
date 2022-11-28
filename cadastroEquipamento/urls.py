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
    path('operacoes/', views.operacoesAtivas, name="operacoesAtivas"),
    path('operacoes/<int:pk>', views.operacao_details, name="operacao_details"),
    path("perifericos/", views.perifericos, name="perifericos"),   
    path('api/', include(route.urls)),
    # path('entrada/', views.entrada, name='entrada'),
] 


  