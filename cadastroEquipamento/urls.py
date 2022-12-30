from django.urls import path, include
from . import views
from .api.views import  DashboardViewMonth 
from rest_framework import routers


route = routers.DefaultRouter()
route.register(r'dashboard/current-month', DashboardViewMonth, basename="api-mes")

urlpatterns = [
    path('', views.dashboard_incidentes, name='home'),
    path('incidente/<slug:chamado>', views.incidente_details, name='incidente_details'),
    path("pesquisar/chamado", views.search_chamado, name="search_chamado"),
    path("pesquisar/operacao", views.search_operacao, name="search_operacao"),
    path('operacoes/', views.operacoesAtivas, name="operacoesAtivas"),
    path('operacoes/<int:pk>', views.operacao_details, name="operacao_details"),
    path('dashboards/', views.dashboards, name="usuarios"),
    path("perifericos/", views.perifericos, name="perifericos"),   
    path('api/', include(route.urls)),
    path('logout/', views.logout_view, name="logout_view"),
    # path('entrada/', views.entrada, name='entrada'),
] 


  