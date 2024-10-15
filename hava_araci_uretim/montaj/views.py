from django.shortcuts import render, redirect
from .models import Assembly, AssemblyPart
from uretim.models import Plane, Part
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.utils import timezone

# uçak montajı için gerekli fonksiyon
def assemble_plane(request):
    # Eğer kullanıcının takımı montaj takımı değilse erişimi engelle
    if request.user.personnel.team.name != 'MONTAJ':
        return HttpResponseForbidden("Bu sayfaya erişim izniniz yoktur.")
    if request.method == 'POST':
        plane_id = request.POST.get('plane_id')  # Seçilen uçağı alıyoruz
        plane = Plane.objects.get(id=plane_id)

        # Uçağın montajında kullanılacak parçaları al
        parts_needed = ['KANAT', 'GOVDE', 'KUYRUK', 'AVIYONIK']  # Montaj için gerekli parçalar
        used_parts = []  # Kullanılan parçaları kaydetmek için

        # Eksik parçaları kontrol et
        missing_parts = []
        for part_type in parts_needed:
            # Seçilen uçağa ait olan ve stokta bulunan parçaları filtreliyoruz
            part = Part.objects.filter(part_type=part_type, stock_quantity__gt=0, plane=plane).first()
            
            # Eğer parça stokta yoksa veya başka bir uçakta kullanıldıysa eksik olarak işaretle
            if not part:
                missing_parts.append(part_type)
            else:
                used_parts.append(part)  # Kullanılabilir parça listesine ekle

        # Eğer eksik parçalar varsa montajı durdur ve kullanıcıya bildir
        if missing_parts:
            messages.error(request, f'Eksik parçalar: {", ".join(missing_parts)}')

            # Formu yeniden render ederken seçili uçağı koruyoruz
            return render(request, 'montaj/assemble_plane.html', {
                'planes': Plane.objects.all(),  # Tüm uçakları tekrar gösteriyoruz
                'selected_plane': plane_id,  # Seçilen uçağı formda tekrar seçili göstermek için
                'missing_parts': missing_parts  # Eksik parçaları gösteriyoruz
            })
        
        # Eğer tüm parçalar mevcutsa montajı başlat
        assembly = Assembly.objects.create(plane=plane, status='TAMAMLANDI')
        for part in used_parts:
            # Her bir parçayı montaja ekle ve stoktan düş
            AssemblyPart.objects.create(assembly=assembly, part=part, quantity_used=1)
            part.stock_quantity -= 1
            part.plane = plane
            part.save()

        messages.success(request, f'{plane.name} başarıyla monte edildi!')
        return redirect('montaj_success')  # Montaj başarıyla tamamlandığında yönlendir

    # Eğer GET isteği yapılıyorsa
    planes = Plane.objects.all()  # Montaj yapılacak uçakları listeliyoruz
    return render(request, 'montaj/assemble_plane.html', {'planes': planes})

# Montaj başarıyla tamamlandığında bu işlev çalışacak
def montaj_success(request):
    return render(request, 'montaj/montaj_success.html')

from django.utils import timezone

def assembly_report(request):
    # Tüm montajları ve ilgili parçaları alıyoruz
    assemblies = Assembly.objects.all().prefetch_related('assemblypart_set')
    
    # Her montaj için kullanılan parçaları topluyoruz
    assembly_data = []
    for assembly in assemblies:
        # Montaj tarihini Türkiye saatine göre ayarlıyoruz
        date_assembled_tz = timezone.localtime(assembly.date_assembled, timezone.get_current_timezone())
        
        parts_used = AssemblyPart.objects.filter(assembly=assembly)
        assembly_data.append({
            'plane': assembly.plane.name,
            'date_assembled': date_assembled_tz.strftime('%d/%m/%Y %H:%M'),  # Türkiye tarih ve saat formatı
            'status': assembly.get_status_display(),
            'parts': parts_used,
        })
    
    return render(request, 'montaj/assembly_report.html', {'assembly_data': assembly_data})

