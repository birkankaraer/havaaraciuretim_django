from django.shortcuts import render, redirect, get_object_or_404
from .models import Personnel
from .forms import PersonnelForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q  # Q nesnesi, çoklu filtreler için kullanılır
from django.contrib.auth.decorators import login_required

@login_required
def personnel_list(request):
    try:
        personnel = Personnel.objects.get(user=request.user)  # Giriş yapan kullanıcıya göre personeli getir
        return render(request, 'personnel_list.html', {'personnel': [personnel]})
    except Personnel.DoesNotExist:
        return redirect('login')  # Eğer personel kaydı yoksa giriş sayfasına yönlendir

# Personel Ekleme
@login_required
def personnel_create(request):
    # Kullanıcıya ait personel olup olmadığını kontrol et
    if Personnel.objects.filter(user=request.user).exists():
        messages.error(request, 'Bu kullanıcıya zaten bir personel atanmış.')
        return redirect('personnel_list')  # Zaten bir personel varsa listeye yönlendir

    if request.method == "POST":
        form = PersonnelForm(request.POST)
        if form.is_valid():
            personnel = form.save(commit=False)
            personnel.user = request.user  # Otomatik olarak giriş yapan kullanıcıyı atıyoruz
            personnel.save()
            return redirect('personnel_list')  # Başarıyla eklendikten sonra listeye yönlendirme
    else:
        form = PersonnelForm()

    return render(request, 'personnel_create.html', {'form': form})


# Personel Güncelleme 
def personnel_update(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)  # Düzenlenecek personeli buluyoruz
    if request.method == "POST":
        form = PersonnelForm(request.POST, instance=personnel)  # Mevcut personel bilgilerini forma yerleştiriyoruz
        if form.is_valid():
            form.save()  # Düzenlenmiş bilgileri kaydediyoruz
            return redirect('personnel_list')  # Başarıyla düzenlendikten sonra listeye yönlendirme
    else:
        form = PersonnelForm(instance=personnel)  # Mevcut bilgileri formda gösteriyoruz

    return render(request, 'personnel_update.html', {'form': form})

# Personel silme işlemi
def personnel_delete(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)  # İlgili personeli getir
    if request.method == 'POST':
        personnel.delete()  # Personeli sil
        return redirect('personnel_list')  # Silme işlemi sonrası personel listesine yönlendir

    return render(request, 'personnel_delete.html', {'personnel': personnel})

def personnel_data(request):
    search_value = request.GET.get('search[value]', '')  # Arama değerini alıyoruz

    # Personelleri sorgularken arama sorgusunu da dahil ediyoruz
    personnels = Personnel.objects.all()

    # Eğer bir arama değeri girildiyse, isme veya takıma göre filtrele
    if search_value:
        personnels = personnels.filter(
            Q(name__icontains=search_value) | Q(team__name__icontains=search_value)
        )

    data = {
        "draw": int(request.GET.get('draw', 1)),
        "recordsTotal": Personnel.objects.count(),  # Tüm personel sayısı
        "recordsFiltered": personnels.count(),  # Filtrelenmiş sonuçların sayısı
        "data": list(personnels.values('id', 'name', 'team__name'))
    }
    
    return JsonResponse(data)

