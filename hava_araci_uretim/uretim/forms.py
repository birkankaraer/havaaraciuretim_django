from django import forms
from .models import Part, Plane

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'part_type', 'stock_quantity', 'plane']  # Uçak seçimi alanını ekliyoruz
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'part_type': forms.Select(attrs={'class': 'form-control'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'plane': forms.Select(attrs={'class': 'form-control'}),  # Uçak seçimi için dropdown
        }
