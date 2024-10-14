"""
URL configuration for hava_araci_uretim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from uretim import views as uretim_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('uretim.urls')),
    path('', uretim_views.home, name='home'),  # Giriş yapmayanlar için anasayfa
    path('login/', include('django.contrib.auth.urls')),
    path('personnel/', include('personnel.urls')),
    path('montaj/', include('montaj.urls')),
    path('uretim/', include('uretim.urls')),
]
