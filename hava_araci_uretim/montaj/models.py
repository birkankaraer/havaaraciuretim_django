from django.db import models
from uretim.models import Plane, Part

# Assembly modelini tanımlıyoruz, bu model montaj işlemlerinin hangi uçak üzerinde yapıldığını ve montajın durumunu tutar.
class Assembly(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)  # Montaj yapılan uçak. Eğer uçak silinirse, ilişkili montaj da silinir.
    date_assembled = models.DateTimeField(auto_now_add=True)    # Montajın tamamlandığı tarih, otomatik olarak şu anki tarih ve saat ile kaydedilir.
    status = models.CharField(
        max_length=20, 
        choices=[('TAMAMLANDI', 'Tamamlandı'), ('EKSİK', 'Eksik')],  # Montaj durumu: Tamamlandı veya Eksik olabilir.
        default='EKSİK'  # Varsayılan montaj durumu Eksik olarak ayarlanmıştır.
    )  

    # __str__ metodu, nesnenin anlamlı bir şekilde yazdırılmasını sağlar.
    def __str__(self):
        return f"{self.plane.name} montajı - {self.get_status_display()}"  # Montaj yapılan uçağın adı ve durumu gösterilir.


# AssemblyPart modeli, her montaj için kullanılan parçaları ve bu parçaların miktarlarını tutar.
class AssemblyPart(models.Model):
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE)  # Hangi montaj işleminde kullanıldığı belirtilen parça.
    part = models.ForeignKey(Part, on_delete=models.CASCADE)  # Kullanılan parça.
    quantity_used = models.IntegerField(default=1)  # Kullanılan parça sayısı, varsayılan olarak 1.

    # __str__ metodu, kullanılan parçanın adı ve adediyle birlikte anlamlı bir şekilde yazdırılmasını sağlar.
    def __str__(self):
        return f"{self.part.name} - {self.quantity_used} adet"
