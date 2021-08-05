from django.shortcuts import render

# Create your views here.
from home.models import Setting
from home_en.models import Setting_en


def index_en(request):
    setting_en = Setting_en.objects.get(pk=2)

    page = "home_en"
    context = {'setting_en': setting_en,
               'page': page
               }
    return render(request, 'index_en.html', context)


