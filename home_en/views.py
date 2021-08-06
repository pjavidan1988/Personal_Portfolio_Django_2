from django.core.mail import EmailMessage
from django.shortcuts import render

# Create your views here.
from home_en.models import Setting_en, Blog_en, Resume_en, Skill_en, otherSkill_en, Education_en, Experience_en


def index_en(request):
    setting_en = Setting_en.objects.get(pk=2)

    page = "home_en"
    context = {'setting_en': setting_en,
               'page': page
               }
    return render(request, 'index_en.html', context)


def resume_en(request):
    resume_en = Resume_en.objects.filter(status="True")
    skills_en = Skill_en.objects.filter(status="True")
    otherskill_en = otherSkill_en.objects.filter()
    education_en = Education_en.objects.filter()
    experience_en = Experience_en.objects.filter()
    setting_en = Setting_en.objects.get(pk=2)

    context = {
        'resume_en': resume_en,
        'setting_en': setting_en,
        'skills_en': skills_en,
        'education_en': education_en,
        'otherskill_en': otherskill_en,
        'experience_en': experience_en,
    }
    return render(request, 'resume_en.html', context)


def contact_en(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        body = name + '\n' + '\n' + '\n' + message + '\n' + '\n' + '\n' + 'From: ' + email

        form = EmailMessage(
            'Message from the site',
            body,
            'message',
            ('p.javidan1988@gmail.com',)
        )
        form.send(fail_silently=False)
    setting_en = Setting_en.objects.get(pk=2)
    context = {
        'setting_en': setting_en,
    }
    return render(request, 'contact_en.html', context)


def blog_en(request):
    blog_en = Blog_en.objects.order_by('title')
    setting_en = Setting_en.objects.get(pk=2)

    context = {
        'blog_en': blog_en,
        'setting_en': setting_en,
    }
    return render(request, 'all_blogs_en.html', context)


def blog_detail_en(request, id):
    blog_en = Blog_en.objects.get(pk=id)
    setting_en = Setting_en.objects.get(pk=2)
    context = {
        'blog_en': blog_en,
        'setting_en': setting_en
    }
    return render(request, 'blog_detail_en.html', context)


