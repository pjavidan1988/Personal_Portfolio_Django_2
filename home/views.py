from django.shortcuts import render
from django.core.mail import EmailMessage

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
    if request.method == 'POST':
        name = request.POST['nameContact']
        email = request.POST['emailContact']
        msg = request.POST['messageContact']
        body = name + '\n' + email + '\n' + msg
        form = EmailMessage(
            'contact form',
            body,
            'test',
            ('p.javidan1988@gmail.com',),
        )
        form.send(fail_silently=False)
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting,
    }
    return render(request, 'contact.html', context)

