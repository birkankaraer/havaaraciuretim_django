from django import forms
from .models import Personnel
from uretim.models import Team
from django.contrib.auth.models import User

# Personel formu, sadece isim ve takım alanlarını içeriyor
class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['name', 'team']  # İsim ve takım bilgileri
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Form kontrol sınıfı eklenmiş input
            'team': forms.Select(attrs={'class': 'form-control'}),  # Takım seçimi dropdown ile yapılacak
        }

# Kullanıcı kayıt formu
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Parola alanı gizli olacak
    confirm_password = forms.CharField(widget=forms.PasswordInput)  # Parola doğrulama alanı
    team = forms.ModelChoiceField(queryset=Team.objects.all(), label="Takım Seçin")  # Takım seçimi için dropdown

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']  # Kullanıcı bilgileri

    # Şifrelerin eşleşip eşleşmediğini kontrol eden fonksiyon
    def clean(self):
        cleaned_data = super().clean()  # Formun temizlenmiş verilerini al
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Şifreler uyuşmazsa hata fırlat
        if password != confirm_password:
            raise forms.ValidationError("Şifreler eşleşmiyor.")
