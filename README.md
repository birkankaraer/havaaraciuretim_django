# Hava Aracı Üretim Uygulaması Dökümantasyonu

## Proje Amacı:
Hava Aracı Üretim Uygulaması, belirli takımlara ayrılmış personellerin uçak üretim sürecini yönetmesi için geliştirilmiştir. Her takımın belirli parçaları üretme yetkisi vardır ve Montaj Takımı, bütün bu parçaları bir araya getirerek uçak montajını gerçekleştirir. Parçaların stok durumu, üretim kapasitesi ve montaj süreçleri kontrol edilir, eksiklik durumlarında uyarılar verilir.

Bu proje, SOLID prensipleri ve DRY prensiplerine uyularak, yazılım mimarisine uygun bir şekilde geliştirilmiştir. Projede modüler yapı ve bağımlılıkların düşük seviyede tutulması hedeflenmiş, her bileşen kendi sorumluluk alanında olacak şekilde organize edilmiştir.

## Uygulama İsterleri
**Parçalar:**
- Kanat
- Gövde
- Kuyruk
- Aviyonik

**Uçak Modelleri:**
- TB2
- TB3
- AKINCI
- KIZILELMA

**Takımlar:**
- Kanat Takımı
- Gövde Takımı
- Kuyruk Takımı
- Aviyonik Takımı
- Montaj Takımı

## Fonksiyonalite
**Personel giriş ekranı:** Personeller sisteme giriş yaparak takımlarına ve rollere göre erişim kazanır.
![personelgiris](https://github.com/user-attachments/assets/45383e9f-648b-47a1-b2ad-5ea6eaf54dad)

**Personelin takımı:** Her personel bir takıma bağlıdır ve birden fazla personel aynı takımda yer alabilir.
![birtakımdabirdenfazlapersonel](https://github.com/user-attachments/assets/9441f702-3fee-4fc5-930e-f5f1e6187ddd)

**Takımların kendi parçalarını üretme, listeleme ve geri dönüşüme gönderme işlemleri (CRUD):** Her takım sadece sorumlu olduğu parçaları üretebilir, listeleyebilir ve stok azaldığında geri dönüşüme gönderebilir.
- Üretme  
![parcauretme](https://github.com/user-attachments/assets/bd9c0bc1-2a79-4e4f-918c-1595ab142388)
- Listeleme  
![parcalisteleme](https://github.com/user-attachments/assets/20b30fee-2421-4851-9abe-a22ec8e3e7e6)
- Geri dönüşüme gönderme  
![parcageridonusum](https://github.com/user-attachments/assets/8a903454-9ff6-478e-b885-d01b35562e79)

**Takımların sadece sorumlulukları dahilindeki parçaları üretmesi:** Her takım, yalnızca sorumlu olduğu parçayı üretir.
![parcauretmekuralı](https://github.com/user-attachments/assets/619c13b0-533f-4f17-ba1d-96c9364027d2)

**Montaj Takımı:** Montaj Takımı, üretilen parçaları kullanarak uçak montajını gerçekleştirir.
![montajbasarılı](https://github.com/user-attachments/assets/9ab843cc-45d8-41a8-98c4-18c23fc6030d)

**Envanterde eksik parça uyarıları:** Eksik parça olduğunda sistem kullanıcıya uyarı verir.
![envantereksikparcalar](https://github.com/user-attachments/assets/e245f009-c28a-42b8-804b-0cc8fa7b9de8)

**Parça-Uçak Eşleşmesi:** Her parça, belirli bir uçağa özeldir.
![ucakmontaj](https://github.com/user-attachments/assets/40574f6e-37bd-4c08-a5e0-7a8e967826c6)

**Kullanılan Parçaların Takibi:** Montaj sonrası kullanılan parçalar ve uçak bilgisi kaydedilir.
![montajrapor](https://github.com/user-attachments/assets/47d61e63-6319-4c23-a64c-38218d672ad6)

**Veritabanı Şeması** Veritabanı şeması.
![veritabanısemasi](https://github.com/user-attachments/assets/cf81239c-a441-415a-9041-95985bab4c45)


## Bonus Özellikler
- **Docker ile Çalışma:** Proje Docker ile ayağa kaldırılabilir.
- **İyi Hazırlanmış Dökümantasyon:** Proje dökümantasyonu ve yorum satırları detaylıdır.
- **Birim Testi:** Temel fonksiyonlar için birim testleri yazılmıştır.
- **DataTable Kullanımı:** Listeleme sayfalarında DataTable kullanılmıştır.
- **Server-side DataTable:** Büyük veri setlerinde performanslı veri işlemleri sağlanmıştır.
- **Asenkron Yapı (Ajax):** Sayfa yenilemeden asenkron işlemler yapılmıştır.
- **İlişkisel Tablolar:** İlişkisel tablolar veritabanında ayrı tutulmuştur.
- **Ekstra Kütüphaneler:** Django Rest Framework ve Swagger kullanılmıştır.
- **Bootstrap, Tailwind, jQuery Kullanımı:** Ön yüz düzenlemelerinde bu teknolojiler kullanılmıştır.
- **API Dokümantasyonu (Swagger):** Tüm API’ler Swagger ile belgelenmiştir.

## Kullanılan Teknolojiler
- **Python**: Uygulama altyapısında kullanılan ana programlama dili.
- **Django**: Web uygulama çerçevesi olarak Django kullanıldı.
- **PostgreSQL**: Veritabanı yönetimi için PostgreSQL kullanıldı.
- **Django Rest Framework**: API geliştirme ve yönetimi için Django Rest Framework kullanıldı.
- **Bootstrap**: Sayfa düzeni ve stil tasarımı için Bootstrap kullanıldı.
- **Tailwind CSS**: Ön yüz tasarımında kullanılan CSS framework.
- **jQuery**: Dinamik ön yüz işlemleri için jQuery kullanıldı.
- **Swagger**: API dokümantasyonunu sağlamak için Swagger kullanıldı.
- **Docker**: Projenin container ortamında çalıştırılması için Docker kullanıldı (opsiyonel).
- **pgAdmin4**: PostgreSQL veritabanı yönetimi için pgAdmin4 kullanıldı.
- **DBDiagram**: Veritabanı tasarımı için dbdiagram.io kullanıldı.
- **ChatGPT**: Kod yapısının planlanması, yorumlanması, düzenlenmesi ve projeye dair yazılımsal sorunları çözme süreçlerinde destek teknolojisi olarak kullanıldı.

## Veritabanı Tasarımı
Veritabanı tasarımı yapılırken dbdiagram.io kullanılarak ilişkiler doğru bir şekilde modellenmiştir. Proje many-to-many ilişkiler ve code-first yaklaşımları kullanarak geliştirilmiştir. Her model, projedeki işlevsellikleri karşılayacak şekilde tasarlanmış ve bu modellemeye uygun olarak PostgreSQL üzerinde yapılandırılmıştır. Veritabanı yönetimi için pgAdmin4 kullanılarak tablo oluşturma, veri ekleme ve SQL sorguları yönetilmiştir. Bu süreçte SQL komutlarıyla veritabanı işlemleri yönetilmiş, veritabanı migration'ları da Django üzerinden gerçekleştirilmiştir.

## SOLID ve DRY Prensiplerine Uyum
Projede yazılım geliştirme süreçlerinde SOLID prensiplerine dikkat edilmiştir. Tek Sorumluluk İlkesi (Single Responsibility Principle), her modelin ve sınıfın sadece tek bir işlevi yerine getirmesi gerektiğini savunur. Buna dayanarak, her sınıfın sorumlulukları belirlenmiş ve birbirinden ayrılmıştır. Aynı zamanda, Don't Repeat Yourself (DRY) prensibiyle tekrarlayan kodlardan kaçınılmış, yeniden kullanılabilirlik ön planda tutulmuştur. Bu sayede modüler ve genişletilebilir bir yapı kurulmuştur.

## ChatGPT Desteği
Bu proje boyunca ChatGPT teknolojisinden büyük ölçüde yararlanıldı. Özellikle aşağıdaki alanlarda ChatGPT aktif olarak kullanıldı:
- **Kod Düzenleme ve Optimize Etme:** Proje boyunca kodların okunabilirliğini artırma, SOLID ve DRY prensiplerine uygun hale getirme konusunda ChatGPT’den destek alındı.
- **Yorum Satırları:** Kod yapısına uygun ve anlamlı yorum satırları eklenmesi sürecinde ChatGPT kullanılarak kodların açıklamaları yazıldı.
- **Dokümantasyon Hazırlama:** Proje dökümantasyonunun düzenlenmesi, eksikliklerin giderilmesi ve açıklamaların netleştirilmesi için ChatGPT’den faydalanıldı.
- **Hataların Çözümü:** Proje geliştirilirken karşılaşılan teknik sorunların çözümü için ChatGPT rehberlik etti ve sorunsuz ilerlemeye katkıda bulundu.
- **Test Yazımı:** Birim testlerin yazımı, fonksiyonların test edilmesi ve yapılandırılması sürecinde ChatGPT destek verdi.

## Projenin Geliştirme Süreci
Projeye başlamadan önce proje gereksinimleri detaylı bir şekilde analiz edilmiş ve gereksinimlere uygun bir geliştirme planı oluşturulmuştur. 

Proje boyunca aşağıdaki adımlar izlenmiştir:
1. **Planlama:** Proje gereksinimlerine göre yazılım mimarisi ve veri modelleme yapılmıştır.
2. **Veritabanı Tasarımı:** Veritabanı ilişkileri dbdiagram.io üzerinde planlanmış, ardından PostgreSQL üzerinde uygulamaya geçirilmiştir.
3. **Modelleme:** Django’nun code-first yaklaşımıyla modeller oluşturulmuş ve many-to-many ilişkiler eklenmiştir.
4. **Uygulama Geliştirme:** Gereksinimlere göre uygulamanın tüm fonksiyonları kodlanmış, her bileşenin sorumluluğu doğru bir şekilde belirlenmiştir.
5. **Testler:** Birim testleri yazılarak kritik fonksiyonların doğru çalıştığından emin olunmuştur.
6. **Dokümantasyon:** Proje boyunca her adım detaylı bir şekilde belgelenmiş ve kod yapısı yorum satırlarıyla açıklanmıştır.
7. **ChatGPT Desteği:** Yukarıda açıklanan alanlarda ChatGPT’den yardım alınarak proje daha verimli bir şekilde tamamlanmıştır.

<h3>Kurulum</h3>

Projeyi klonlayın
```
git clone
```

Proje dizine gidin
```
cd havaaraciuretim_django
```

Proje bağımlılıklarını yükleyin
```
pip install -r requirements.txt
```

setting.py dosyasında veritabanı bağlantısı ayarlarınızı yapın.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hava_araci_uretim', # PostgreSQL veritabanı adı
        'USER': 'postgres', # PostgreSQL kullanıcı adı
        'PASSWORD': 'Data1234', # PostgreSQL şifre
        'HOST': 'localhost', # Yerel PostgreSQL sunucusu
        'PORT': '5432', # PostgreSQL port numarası
    }
}
```
Migration işlemlerini yapalım

```
python manage.py migrate
```

Çalıştıralım
```
 python manage.py runserver
```

<h3>Docker ile Projeyi Ayağa Kaldırma</h3>
Proje Docker ile çalıştırılmak üzere yapılandırılmıştır. Gerekli adımları izleyerek projeyi Docker üzerinde ayağa kaldırabilirsiniz.

## Sonuç:
Proje, tüm gereksinimleri ve bonus özellikleri yerine getirmekte olup, genişletilebilir altyapısı ve detaylı dokümantasyonu ile sorunsuz bir üretim yönetim sistemi sunmaktadır. Bu süreçte ChatGPT'nin büyük katkılarıyla proje daha hızlı ve verimli bir şekilde tamamlanmıştır.
