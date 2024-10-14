from django import forms
from .models import Personnel

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['name', 'team']  # Sadece ismi ve takımı alıyoruz
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-control'}),
        }
