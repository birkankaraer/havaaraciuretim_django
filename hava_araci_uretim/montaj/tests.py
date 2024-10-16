from django.test import TestCase
from uretim.models import Plane, Part, Team
from .models import Assembly, AssemblyPart

# Bu sayfada montaj uygulamasının testlerini yazıyoruz.
class AssemblyModelTest(TestCase):
    
    def setUp(self):
        # Testlerin başlamasından önce gerekli verileri oluşturuyoruz
        # Takımları oluştur
        self.kanat_team = Team.objects.create(name='KANAT')
        self.govde_team = Team.objects.create(name='GOVDE')

        # Uçakları oluştur
        self.tb2_plane = Plane.objects.create(name='TB2')

        # Parçaları oluştur
        self.kanat_part = Part.objects.create(name='Kanat 1', part_type='KANAT', stock_quantity=5, team=self.kanat_team)
        self.govde_part = Part.objects.create(name='Gövde 1', part_type='GOVDE', stock_quantity=3, team=self.govde_team)
    
    def test_assembly_creation(self):
        # Montaj oluşturma testi
        # Bir montaj (assembly) kaydı oluşturuyoruz ve bu montaja bir parça ekliyoruz
        assembly = Assembly.objects.create(plane=self.tb2_plane, status='TAMAMLANDI')
        AssemblyPart.objects.create(assembly=assembly, part=self.kanat_part, quantity_used=1)
        
        # Montajın başarıyla oluşturulup oluşturulmadığını kontrol ediyoruz
        self.assertEqual(Assembly.objects.count(), 1)  # Sadece 1 montaj kaydı olmalı
        self.assertEqual(assembly.status, 'TAMAMLANDI')  # Montaj durumu doğru olmalı
    
    def test_assembly_missing_parts(self):
        # Eksik parça testi
        # Bu testte, stokta olmayan bir parçayı test ediyoruz.
        self.kanat_part.stock_quantity = 0  # Kanat parçasının stoğunu sıfırlıyoruz
        self.kanat_part.save()

        # Montaj için gerekli parçaları belirliyoruz
        parts_needed = ['KANAT', 'GOVDE']

        # Stokta olmayan parçaları kontrol ediyoruz
        missing_parts = [part_type for part_type in parts_needed if not Part.objects.filter(part_type=part_type, stock_quantity__gt=0).exists()]

        # Kanat parçasının eksik olduğunu ve gövde parçasının eksik olmadığını test ediyoruz
        self.assertIn('KANAT', missing_parts)  # Kanat eksik olmalı
        self.assertNotIn('GOVDE', missing_parts)  # Gövde eksik olmamalı
