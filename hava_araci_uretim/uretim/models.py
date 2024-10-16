from django.db import models

# Parça (Part) modelini tanımlıyoruz, her parçanın adı, tipi, stok miktarı ve ilişkili takımı var.
class Part(models.Model):
    name = models.CharField(max_length=100)  # Parçanın adı
    part_type = models.CharField(max_length=50, choices=[('KANAT', 'KANAT'), ('GOVDE', 'GOVDE'), ('KUYRUK', 'KUYRUK'), ('AVIYONIK', 'AVIYONIK')])  # Parça türü
    stock_quantity = models.IntegerField(default=0)  # Stok miktarı
    team = models.ForeignKey('uretim.Team', on_delete=models.CASCADE)  # Parçanın bağlı olduğu takım
    plane = models.ForeignKey('uretim.Plane', on_delete=models.SET_NULL, null=True, blank=True)  # Parçanın kullanıldığı uçak, isteğe bağlı

    def __str__(self):
        return self.name  # Parçanın adını döndürür

# Uçak (Plane) modelini tanımlıyoruz, uçak modelleri ve parça ilişkileri burada tutulur.
class Plane(models.Model):
    PLANE_MODELS = (
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('AKINCI', 'Akıncı'),
        ('KIZILELMA', 'Kızılelma'),
    )
    
    name = models.CharField(max_length=50, choices=PLANE_MODELS)  # Uçağın adı ve modeli
    parts = models.ManyToManyField('Part', through='PlanePart', related_name='planes')  # Parça ile ilişki

    def __str__(self):
        return self.name  # Uçağın adını döndürür

# Takım (Team) modelini tanımlıyoruz, her takımın adı ve türü var.
class Team(models.Model):
    TEAM_TYPES = (
        ('KANAT', 'Kanat Takımı'),
        ('GOVDE', 'Gövde Takımı'),
        ('KUYRUK', 'Kuyruk Takımı'),
        ('AVIYONIK', 'Aviyonik Takımı'),
        ('MONTAJ', 'Montaj Takımı'),
    )
    
    name = models.CharField(max_length=100, choices=TEAM_TYPES)  # Takım adı ve türü

    def __str__(self):
        return self.name  # Takımın adını döndürür

# Uçak ve Parça arasında ilişki kuran PlanePart modeli, hangi parçaların hangi uçakta kullanıldığını takip eder.
class PlanePart(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)  # İlgili uçak
    part = models.ForeignKey(Part, on_delete=models.CASCADE)  # İlgili parça
    quantity_used = models.IntegerField(default=1)  # Kullanılan parça sayısı

    class Meta:
        unique_together = ('plane', 'part')  # Aynı uçakta bir parçanın bir defa kullanılması kuralı
