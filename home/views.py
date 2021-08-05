from django.shortcuts import render

# Create your views here.
from home.models import Setting, Resume, Skill, Education, otherSkill, Experience


def index(request):
    setting = Setting.objects.get(pk=1)

    page = "home"
    context = {'setting': setting,
               }
    return render(request, 'index.html', context)


def resume(request):
    resume = Resume.objects.filter(status="True")
    skills = Skill.objects.filter(status="True")
    otherskill = otherSkill.objects.filter()
    education = Education.objects.filter()
    experience = Experience.objects.filter()
    setting = Setting.objects.get(pk=1)

    context = {
        'resume': resume,
        'setting': setting,
        'skills' : skills,
        'education' : education,
        'otherskill' : otherskill,
        'experience' : experience,
    }
    return render(request, 'resume.html', context)

def contact(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting,
    }
    return render(request, 'contact.html', context)

