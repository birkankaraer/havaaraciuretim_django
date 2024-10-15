from django.urls import path
from . import views

urlpatterns = [
    path('', views.personnel_list, name='personnel_list'), # Personel listeleme için URL
    path('create/', views.personnel_create, name='personnel_create'), # Personel ekleme için URL
    path('update/<int:pk>/', views.personnel_update, name='personnel_update'), # Personel düzenleme için URL
    path('delete/<int:pk>/', views.personnel_delete, name='personnel_delete'), # Personel silme için URL
    path('data/', views.personnel_data, name='personnel_data'), # DataTable için
    path('register/', views.register, name='register'),  # Kayıt olma url'si
]
