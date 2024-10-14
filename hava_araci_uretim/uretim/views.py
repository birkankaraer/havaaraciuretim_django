from rest_framework import viewsets
from .models import Part, Plane, Team
from .serializers import PartSerializer, PlaneSerializer, TeamSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect,  get_object_or_404
from .forms import PartForm
from django.contrib.auth.decorators import login_required


# Parça (Part) modeli için ViewSet
class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

# Uçak (Plane) modeli için ViewSet
class PlaneViewSet(viewsets.ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer

# Takım (Team) modeli için ViewSet
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('personnel_list')  # Giriş başarılı olursa anasayfaya yönlendir
        else:
            messages.error(request, 'Kullanıcı adı veya parola yanlış!')  # Hata mesajı
    
    return render(request, 'registration/login.html')  # GET isteğinde login sayfasını göster

def custom_logout_view(request):
    logout(request)
    return redirect('home')  # Çıkış yaptıktan sonra ana sayfaya yönlendir

def home(request):
    if request.user.is_authenticated:
        return redirect('personnel_list')  # Eğer kullanıcı giriş yaptıysa personel listesine yönlendir
    return render(request, 'home.html')  # Giriş yapmayanlar için home sayfasını döndür


@login_required  # Kullanıcının giriş yapmasını zorunlu kılar
def part_list(request):
    try:
        team = request.user.personnel.team  # Kullanıcının takımını alıyoruz
        parts = Part.objects.filter(team=team)  # Yalnızca kullanıcının takımına ait parçaları listeliyoruz
        return render(request, 'parts/part_list.html', {'parts': parts})
    except AttributeError:
        # Eğer user'ın personnel objesi yoksa veya başka bir sorun varsa hata fırlatılır
        messages.error(request, 'Personel bilgilerinize ulaşılamıyor.')
        return redirect('login')  # Eğer bir hata varsa giriş sayfasına yönlendirin

# Parça Üretme (Ekleme)
def part_create(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            part = form.save(commit=False)
            user_team = request.user.personnel.team

            # Takımın sorumlu olduğu parça tiplerini kontrol ediyoruz
            allowed_part_types = {
                'KANAT': 'KANAT',
                'GOVDE': 'GOVDE',
                'KUYRUK': 'KUYRUK',
                'AVIYONIK': 'AVIYONIK',
            }

            # Kullanıcının takımına uygun parça tipini belirliyoruz
            team_allowed_part_type = allowed_part_types.get(user_team.name)

            # Eğer eklenmek istenen parça kullanıcının sorumlu olduğu takımda değilse hata veriyoruz
            if part.part_type != team_allowed_part_type:
                messages.error(request, f'{user_team.name} sadece {team_allowed_part_type} üretebilir.')
                return render(request, 'parts/part_create.html', {'form': form})

            # Eğer stok miktarı negatifse veya sıfırsa hata veriyoruz
            if part.stock_quantity <= 0:
                messages.error(request, 'Stok miktarı 1 veya daha fazla olmalıdır.')
                return render(request, 'parts/part_create.html', {'form': form})

            # Parçanın başka bir uçakta kullanılıp kullanılmadığını kontrol ediyoruz
            # Ancak aynı uçak için farklı türde parçalar üretilmesine izin veriyoruz
            if part.plane:
                existing_parts = Part.objects.filter(plane=part.plane, part_type=part.part_type).exists()
                if existing_parts:
                    messages.error(request, 'Bu parça zaten başka bir uçakta kullanılmış.')
                    return render(request, 'parts/part_create.html', {'form': form})

            # Eğer her şey uygunsa parçayı kaydediyoruz
            part.team = user_team  # Parça kullanıcının takımına atanıyor
            part.save()
            messages.success(request, 'Parça başarıyla üretildi ve stoğa eklendi.')
            return redirect('part_list')
    else:
        form = PartForm()

    return render(request, 'parts/part_create.html', {'form': form})


# Parça Silme (Geri Dönüşüme Gönderme)
def part_delete(request, pk):
    part = get_object_or_404(Part, pk=pk)
    if part.team == request.user.personnel.team:  # Kullanıcı yalnızca kendi takımına ait parçayı silebilir
        part.delete()
    return redirect('part_list')
