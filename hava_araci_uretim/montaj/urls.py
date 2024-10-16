from django.urls import path
from . import views

# Montaj uygulamasına ait URL yapılandırmalarını belirliyoruz.
urlpatterns = [
    # Uçak montajı için URL. 'assemble_plane' fonksiyonu çalıştırılır.
    path('assemble/', views.assemble_plane, name='assemble_plane'),  
    
    # Montaj başarıyla tamamlandığında yönlendirilecek URL. 'montaj_success' fonksiyonu çalıştırılır.
    path('success/', views.montaj_success, name='montaj_success'),
    
    # Montaj raporu görüntülemek için URL. 'assembly_report' fonksiyonu çalıştırılır.
    path('montaj/rapor/', views.assembly_report, name='assembly_report'),
]
