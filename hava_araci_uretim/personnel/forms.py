from django import forms
from .models import Personnel
from uretim.models import Team
from django.contrib.auth.models import User

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['name', 'team']  # Sadece ismi ve takımı alıyoruz
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-control'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    team = forms.ModelChoiceField(queryset=Team.objects.all(), label="Takım Seçin")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Şifreler eşleşmiyor.")
