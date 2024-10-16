from django.apps import AppConfig

# Montaj uygulamasının yapılandırma sınıfı
class MontajConfig(AppConfig):
    # Varsayılan otomatik birincil anahtar alanını belirtiyoruz (BigAutoField, büyük tamsayı birincil anahtar alanı sağlar)
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Bu uygulamanın adını tanımlıyoruz
    name = 'montaj'
