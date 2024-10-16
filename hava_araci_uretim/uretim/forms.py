from django import forms
from .models import Part, Plane

# Parça formunu tanımlıyoruz, bu form Part modeline bağlıdır.
class PartForm(forms.ModelForm):
    class Meta:
        model = Part  # Formda kullanılacak model Part
        fields = ['name', 'part_type', 'stock_quantity', 'plane']  # Formda gösterilecek alanlar
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Parça adı için text input
            'part_type': forms.Select(attrs={'class': 'form-control'}),  # Parça tipi için dropdown menü
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control'}),  # Stok miktarı için sayısal input
            'plane': forms.Select(attrs={'class': 'form-control'}),  # Uçak seçimi için dropdown menü
        }
