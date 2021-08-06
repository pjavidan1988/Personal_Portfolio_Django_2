from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.
from home.models import Setting, Resume, Skill, Education, otherSkill, Experience, Blog


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
        'skills': skills,
        'education': education,
        'otherskill': otherskill,
        'experience': experience,
    }
    return render(request, 'resume.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        body = name + '\n' + '\n' + '\n' + message + '\n' + '\n' + '\n' + 'From: ' + email

        form = EmailMessage(
            'پیام از طرف سایت',
            body,
            'message',
            ('p.javidan1988@gmail.com',)
        )
        form.send(fail_silently=False)
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting,
    }
    return render(request, 'contact.html', context)


def blog(request):
    blog = Blog.objects.order_by('title')
    setting = Setting.objects.get(pk=1)

    context = {
        'blog': blog,
        'setting': setting,
    }
    return render(request, 'all_blogs.html', context)


def blog_detail(request, id):
    blog = Blog.objects.get(pk=id)
    setting = Setting.objects.get(pk=1)
    context = {
        'blog': blog,
        'setting': setting
    }
    return render(request, 'blog_detail.html', context)
