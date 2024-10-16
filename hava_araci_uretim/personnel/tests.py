from django.test import TestCase
from django.contrib.auth.models import User
from .models import Personnel
from .forms import PersonnelForm  # Eksik olan import
from uretim.models import Team

class PersonnelModelTest(TestCase):
    
    def setUp(self):
        # Takımları oluştur
        self.kanat_team = Team.objects.create(name='KANAT')
        
        # Kullanıcıları oluştur
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    def test_personnel_creation(self):
        # Personel oluşturma testi
        personnel = Personnel.objects.create(user=self.user, name='Test Personel', team=self.kanat_team)
        
        self.assertEqual(Personnel.objects.count(), 1)
        self.assertEqual(personnel.name, 'Test Personel')
        self.assertEqual(personnel.team.name, 'KANAT')
    
    def test_personnel_form_valid(self):
        # Formun geçerli olduğu durumu test et
        data = {
            'name': 'Test Personel',
            'team': self.kanat_team.id,
        }
        form = PersonnelForm(data=data)
        self.assertTrue(form.is_valid())

    def test_personnel_form_invalid(self):
        # Formun geçersiz olduğu durumu test et
        data = {
            'name': '',  # Name boş bırakıldığında
            'team': self.kanat_team.id,
        }
        form = PersonnelForm(data=data)
        self.assertFalse(form.is_valid())
