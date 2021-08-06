from django.contrib import admin

# Register your models here.

from django.contrib import admin

from django.contrib import admin

# Register your models here.
from home.models import Setting, Resume, Skill, Education, otherSkill, Experience, Blog
from home_en.models import Setting_en, Resume_en, Blog_en, otherSkill_en, Experience_en, Education_en, Skill_en


class Setting_enAdmin(admin.ModelAdmin):
    list_display = ['name', 'update_at', 'status']


class Resume_enSkill_enInline(admin.TabularInline):
    model = Skill_en
    readonly_fields = ('id',)
    extra = 1


class Resume_enEducation_enInline(admin.TabularInline):
    model = Education_en
    readonly_fields = ('id',)
    extra = 1


class Resume_enExperience_enInline(admin.TabularInline):
    model = Experience_en
    readonly_fields = ('id',)
    extra = 1


class Resume_enotherSkill_enInline(admin.TabularInline):
    model = otherSkill_en
    readonly_fields = ('id',)
    extra = 1


class Resume_enAdmin(admin.ModelAdmin):
    list_display = ['university', 'update_at', 'status']
    inlines = [Resume_enSkill_enInline, Resume_enEducation_enInline, Resume_enotherSkill_enInline, Resume_enExperience_enInline]



class Blog_enAdmin(admin.ModelAdmin):
    list_display = ['title', 'update_at']
    list_filter = ['update_at']


admin.site.register(Setting_en, Setting_enAdmin)
admin.site.register(Resume_en, Resume_enAdmin)
admin.site.register(Blog_en, Blog_enAdmin)
