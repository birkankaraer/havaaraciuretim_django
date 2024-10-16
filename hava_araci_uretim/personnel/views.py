from django.shortcuts import render, redirect, get_object_or_404
from .models import Personnel
from .forms import PersonnelForm, UserRegistrationForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q  # Çoklu filtreleme işlemleri için Q nesnesi kullanılır
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Kullanıcı kayıt fonksiyonu
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Parola şifreleniyor
            user.save()

            # Kullanıcıya personel kaydı oluşturulup takıma atanıyor
            team = form.cleaned_data['team']
            Personnel.objects.create(user=user, team=team, name=user.get_full_name())

            # Kayıt sonrası otomatik giriş işlemi
            login(request, user)
            return redirect('personnel_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# Personel listeleme fonksiyonu, giriş yapmış kullanıcıya özel
@login_required
def personnel_list(request):
    try:
        personnel = Personnel.objects.get(user=request.user)  # Giriş yapan kullanıcıya ait personel bilgileri
        return render(request, 'personnel_list.html', {'personnel': [personnel]})
    except Personnel.DoesNotExist:
        return redirect('login')  # Personel kaydı yoksa giriş sayfasına yönlendirme

# Yeni personel ekleme fonksiyonu
@login_required
def personnel_create(request):
    # Kullanıcının zaten bir personeli olup olmadığını kontrol et
    if Personnel.objects.filter(user=request.user).exists():
        messages.error(request, 'Bu kullanıcıya zaten bir personel atanmış.')
        return redirect('personnel_list')

    if request.method == "POST":
        form = PersonnelForm(request.POST)
        if form.is_valid():
            personnel = form.save(commit=False)
            personnel.user = request.user  # Giriş yapan kullanıcı otomatik atanır
            personnel.save()
            return redirect('personnel_list')  # Ekleme başarılıysa personel listesine yönlendirme
    else:
        form = PersonnelForm()

    return render(request, 'personnel_create.html', {'form': form})

# Personel düzenleme fonksiyonu
@login_required
def personnel_update(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)  # Düzenlenecek personel bilgisi getiriliyor
    if request.method == "POST":
        form = PersonnelForm(request.POST, instance=personnel)  # Mevcut bilgiler forma yükleniyor
        if form.is_valid():
            form.save()  # Düzenlemeler kaydediliyor
            return redirect('personnel_list')
    else:
        form = PersonnelForm(instance=personnel)  # Mevcut bilgiler formda gösteriliyor

    return render(request, 'personnel_update.html', {'form': form})

# Personel silme fonksiyonu
@login_required
def personnel_delete(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)  # Silinecek personel bilgisi
    if request.method == 'POST':
        personnel.delete()  # Personel siliniyor
        return redirect('personnel_list')

    return render(request, 'personnel_delete.html', {'personnel': personnel})

# DataTable için JSON formatında personel verilerini döndüren fonksiyon
@login_required
def personnel_data(request):
    search_value = request.GET.get('search[value]', '')  # Arama değeri alınıyor

    # Arama değerine göre personel bilgileri sorgulanıyor
    personnels = Personnel.objects.all()

    if search_value:
        personnels = personnels.filter(
            Q(name__icontains=search_value) | Q(team__name__icontains=search_value)  # İsim veya takıma göre filtreleme
        )

    # DataTable için gereken veriler
    data = {
        "draw": int(request.GET.get('draw', 1)),
        "recordsTotal": Personnel.objects.count(),  # Toplam personel sayısı
        "recordsFiltered": personnels.count(),  # Filtrelenmiş personel sayısı
        "data": list(personnels.values('id', 'name', 'team__name'))  # JSON formatında personel bilgileri
    }
    
    return JsonResponse(data)
