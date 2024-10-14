from django.db import models
from uretim.models import Plane, Part

# Bu model, montaj işlemlerinin hangi uçak üzerinde yapıldığını ve hangi parçaların kullanıldığını tutacak.
class Assembly(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)  # Montaj yapılan uçak
    date_assembled = models.DateTimeField(auto_now_add=True)    # Montajın tamamlandığı tarih
    status = models.CharField(
        max_length=20, 
        choices=[('TAMAMLANDI', 'Tamamlandı'), ('EKSİK', 'Eksik')], 
        default='EKSİK'
    )  # Montaj durumu

    def __str__(self):
        return f"{self.plane.name} montajı - {self.get_status_display()}"

class AssemblyPart(models.Model):
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity_used = models.IntegerField(default=1)  # Kullanılan parça sayısı

    def __str__(self):
        return f"{self.part.name} - {self.quantity_used} adet"
