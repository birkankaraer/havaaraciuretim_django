from django.shortcuts import render, redirect
from .models import Assembly, AssemblyPart
from uretim.models import Plane, Part
from django.contrib import messages

def assemble_plane(request):
    if request.method == 'POST':
        plane_id = request.POST.get('plane_id')  # Seçilen uçağı alıyoruz
        plane = Plane.objects.get(id=plane_id)

        # Uçağın montajında kullanılacak parçaları al
        parts_needed = ['KANAT', 'GOVDE', 'KUYRUK', 'AVIYONIK']  # Montaj için gerekli parçalar
        used_parts = []  # Kullanılan parçaları kaydetmek için

        # Eksik parçaları kontrol et
        missing_parts = []
        for part_type in parts_needed:
            # Parçanın hem stokta olup olmadığını hem de uçakta kullanılıp kullanılmadığını kontrol ediyoruz
            part = Part.objects.filter(part_type=part_type, stock_quantity__gt=0).first()
            
            # Eğer parça stokta yoksa eksik olarak işaretle
            if not part:
                missing_parts.append(part_type)
            else:
                used_parts.append(part)  # Kullanılabilir parça listesine ekle

        # Eğer eksik parçalar varsa montajı durdur ve kullanıcıya bildir
        if missing_parts:
            messages.error(request, f'Eksik parçalar: {", ".join(missing_parts)}')

            # Formu yeniden render ederken seçili uçağı koruyoruz
            return render(request, 'montaj/assemble_plane.html', {
                'plane': plane,  # Seçilen uçağı formda tekrar göstermek için context'e ekliyoruz
                'missing_parts': missing_parts,
                'planes': Plane.objects.all(),  # Tüm uçakları tekrar gösteriyoruz
                'selected_plane': plane_id  # Seçilen uçağı formda tekrar seçili göstermek için
            })
        
        # Eğer tüm parçalar mevcutsa montajı başlat
        assembly = Assembly.objects.create(plane=plane, status='TAMAMLANDI')
        for part in used_parts:
            # Her bir parçayı montaja ekle ve stoktan düş
            AssemblyPart.objects.create(assembly=assembly, part=part, quantity_used=1)
            part.stock_quantity -= 1
            part.plane = plane  # Parçayı uçakla ilişkilendiriyoruz
            part.save()

        messages.success(request, f'{plane.name} başarıyla monte edildi!')
        return redirect('montaj_success')  # Montaj başarıyla tamamlandığında yönlendir

    # Eğer GET isteği yapılıyorsa
    planes = Plane.objects.all()  # Montaj yapılacak uçakları listeliyoruz
    return render(request, 'montaj/assemble_plane.html', {'planes': planes})



# Montaj başarıyla tamamlandığında bu işlev çalışacak
def montaj_success(request):
    return render(request, 'montaj/montaj_success.html')
