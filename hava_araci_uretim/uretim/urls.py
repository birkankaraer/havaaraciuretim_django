from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PartViewSet, PlaneViewSet, TeamViewSet, custom_login_view
from django.contrib.auth import views as auth_views

# Router'ı tanımlıyoruz
router = DefaultRouter()
router.register(r'parts-api', PartViewSet)
router.register(r'planes-api', PlaneViewSet)
router.register(r'teams-api', TeamViewSet, basename='team')

# URL'leri tanımlıyoruz
urlpatterns = [
    # API yollarını 'api/' prefix'i ile sınırlıyoruz
    path('api/', include(router.urls)),  
    
    # Giriş ve çıkış işlemleri için url tanımlamaları
    path('login/', custom_login_view, name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    
    # Parça işlemleri için geleneksel view yolları
    path('parts/', views.part_list, name='part_list'),
    path('parts/create/', views.part_create, name='part_create'),
    path('parts/delete/<int:pk>/', views.part_delete, name='part_delete'),
    path('team-parts/', views.team_parts_list, name='team_parts_list'),  # Takım parçaları için yol
]
