# uretim/tests.py
from django.test import TestCase
from .models import Team, Plane

class TeamModelTest(TestCase):
    
    def setUp(self):
        Team.objects.create(name='KANAT')
        Team.objects.create(name='GOVDE')

    def test_team_name(self):
        kanat_team = Team.objects.filter(name='KANAT').first()
        govde_team = Team.objects.filter(name='GOVDE').first()
        self.assertEqual(kanat_team.name, 'KANAT')
        self.assertEqual(govde_team.name, 'GOVDE')

class PlaneModelTest(TestCase):
    
    def setUp(self):
        Plane.objects.create(name='TB2')
        Plane.objects.create(name='AKINCI')

    def test_plane_name(self):
        tb2_plane = Plane.objects.filter(name='TB2').first()
        akinci_plane = Plane.objects.filter(name='AKINCI').first()
        self.assertEqual(tb2_plane.name, 'TB2')
        self.assertEqual(akinci_plane.name, 'AKINCI')
