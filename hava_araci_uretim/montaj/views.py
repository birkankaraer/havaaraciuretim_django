from django.shortcuts import render, redirect
from .models import Assembly, AssemblyPart
from uretim.models import Plane, Part
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Uçak montajı işlemi için gerekli fonksiyon
@login_required  # Bu fonksiyonun kullanılması için kullanıcı girişi yapılması gerekiyor
def assemble_plane(request):
    # Eğer kullanıcının takımı montaj takımı değilse, yetkisiz erişimi engelle
    if request.user.personnel.team.name != 'MONTAJ':
        return HttpResponseForbidden("Bu sayfaya erişim izniniz yoktur.")

    # POST isteği yapıldığında montaj işlemini gerçekleştir
    if request.method == 'POST':
        plane_id = request.POST.get('plane_id')  # Montaj yapılacak uçağı seç
        plane = Plane.objects.get(id=plane_id)

        # Uçağın montajında gerekli olan parçaların listesi
        parts_needed = ['KANAT', 'GOVDE', 'KUYRUK', 'AVIYONIK']  
        used_parts = []  # Kullanılabilir parçaları toplamak için liste

        # Eksik parçaları kontrol etme
        missing_parts = []
        for part_type in parts_needed:
            # Uçağa uygun ve stokta olan parçaları bul
            part = Part.objects.filter(part_type=part_type, stock_quantity__gt=0, plane=plane).first()
            
            # Eğer parça yoksa veya stokta değilse eksik listesine ekle
            if not part:
                missing_parts.append(part_type)
            else:
                used_parts.append(part)  # Uygun parçaları kullanılanlar listesine ekle

        # Eksik parçalar varsa montaj işlemini durdur ve kullanıcıya hata mesajı göster
        if missing_parts:
            messages.error(request, f'Eksik parçalar: {", ".join(missing_parts)}')

            # Eksik parçalarla beraber formu tekrar göster
            return render(request, 'montaj/assemble_plane.html', {
                'planes': Plane.objects.all(),  # Tüm uçakları tekrar formda göster
                'selected_plane': plane_id,  # Seçilen uçağı koru
                'missing_parts': missing_parts  # Eksik parçaları göster
            })
        
        # Tüm parçalar mevcutsa montajı başlat
        assembly = Assembly.objects.create(plane=plane, status='TAMAMLANDI')
        for part in used_parts:
            # Parçaları montaja ekle ve stok miktarını güncelle
            AssemblyPart.objects.create(assembly=assembly, part=part, quantity_used=1)
            part.stock_quantity -= 1
            part.plane = plane
            part.save()

        # Başarılı montaj mesajı göster ve başarı sayfasına yönlendir
        messages.success(request, f'{plane.name} başarıyla monte edildi!')
        return redirect('montaj_success')  # Montaj başarıyla tamamlandığında yönlendir

    # GET isteği yapıldığında montaj yapılacak uçakları listele
    planes = Plane.objects.all()  # Tüm uçakları getir
    return render(request, 'montaj/assemble_plane.html', {'planes': planes})

# Montaj başarıyla tamamlandığında çalışan fonksiyon
@login_required  # Kullanıcı girişi gereklidir
def montaj_success(request):
    return render(request, 'montaj/montaj_success.html')


# Montaj raporu oluşturma fonksiyonu
@login_required  # Kullanıcı girişi gereklidir
def assembly_report(request):
    # Tüm montajları ve montajlarda kullanılan parçaları getir
    assemblies = Assembly.objects.all().prefetch_related('assemblypart_set')
    
    # Her montaj için kullanılan parçaları ve montaj tarihini topluyoruz
    assembly_data = []
    for assembly in assemblies:
        # Montaj tarihini yerel saat dilimine göre ayarla (Türkiye saati)
        date_assembled_tz = timezone.localtime(assembly.date_assembled, timezone.get_current_timezone())
        
        # Montajda kullanılan parçaları listele
        parts_used = AssemblyPart.objects.filter(assembly=assembly)
        assembly_data.append({
            'plane': assembly.plane.name,
            'date_assembled': date_assembled_tz.strftime('%d/%m/%Y %H:%M'),  # Tarihi ve saati Türkiye formatında göster
            'status': assembly.get_status_display(),  # Montaj durumunu göster
            'parts': parts_used,  # Kullanılan parçalar
        })
    
    # Montaj raporunu şablonda göster
    return render(request, 'montaj/assembly_report.html', {'assembly_data': assembly_data})
