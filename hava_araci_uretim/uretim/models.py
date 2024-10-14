from django.db import models

# Parça modelini tanımlıyoruz.
class Part(models.Model):
    name = models.CharField(max_length=100)
    part_type = models.CharField(max_length=50, choices=[('KANAT', 'KANAT'), ('GOVDE', 'GOVDE'), ('KUYRUK', 'KUYRUK'), ('AVIYONIK', 'AVIYONIK')])
    stock_quantity = models.IntegerField(default=0)  # Stok miktarı
    team = models.ForeignKey('uretim.Team', on_delete=models.CASCADE)
    plane = models.ForeignKey('uretim.Plane', on_delete=models.SET_NULL, null=True, blank=True)  # Parçanın kullanıldığı uçak

    def __str__(self):
        return self.name

class Plane(models.Model):
    PLANE_MODELS = (
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('AKINCI', 'Akıncı'),
        ('KIZILELMA', 'Kızılelma'),
    )

    name = models.CharField(max_length=50, choices=PLANE_MODELS)
    parts = models.ManyToManyField('Part', through='PlanePart', related_name='planes')

    def __str__(self):
        return self.name

class Team(models.Model):
    TEAM_TYPES = (
        ('KANAT', 'Kanat Takımı'),
        ('GOVDE', 'Gövde Takımı'),
        ('KUYRUK', 'Kuyruk Takımı'),
        ('AVIYONIK', 'Aviyonik Takımı'),
        ('MONTAJ', 'Montaj Takımı'),
    )

    name = models.CharField(max_length=100, choices=TEAM_TYPES)

    def __str__(self):
        return self.name

class PlanePart(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity_used = models.IntegerField(default=1)

    class Meta:
        unique_together = ('plane', 'part')
