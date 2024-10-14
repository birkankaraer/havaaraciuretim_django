from django.urls import path
from . import views

urlpatterns = [
    path('assemble/', views.assemble_plane, name='assemble_plane'),
    path('success/', views.montaj_success, name='montaj_success'),
]
