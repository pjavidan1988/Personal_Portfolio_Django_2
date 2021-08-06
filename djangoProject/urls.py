"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from home import views
from home_en import views as Home_enviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('home_en/', include('home_en.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>', views.blog_detail, name='blog_detail'),

    path('resume_en/', Home_enviews.resume_en, name='resume_en'),
    path('contact_en/', Home_enviews.contact_en, name='contact_en'),
    path('blog_en/', Home_enviews.blog_en, name='blog_en'),
    path('blog_en/<int:id>', Home_enviews.blog_detail_en, name='blog_detail_en'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
