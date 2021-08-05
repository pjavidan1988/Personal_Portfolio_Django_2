from django.urls import path

from . import views

urlpatterns = [
    # home_en/
    path('', views.index_en, name='index_en'),
]