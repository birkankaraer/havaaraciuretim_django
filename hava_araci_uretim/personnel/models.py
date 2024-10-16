from django.db import models
from django.contrib.auth.models import User

# Personel modelini tanımlıyoruz
class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # User modeline bağlantı
    name = models.CharField(max_length=100)  # Personel ismi
    team = models.ForeignKey('uretim.Team', on_delete=models.CASCADE)  # Personelin ait olduğu takım

    # String olarak personel ismini döndüren fonksiyon
    def __str__(self):
        return self.name
