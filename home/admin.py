from django.contrib import admin

# Register your models here.
from home.models import Setting, Resume, Skill, Education, otherSkill, Experience, Blog


class SettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'update_at', 'status']


class ResumeSkillInline(admin.TabularInline):
    model = Skill
    readonly_fields = ('id',)
    extra = 1


class ResumeEducationInline(admin.TabularInline):
    model = Education
    readonly_fields = ('id',)
    extra = 1


class ResumeExperienceInline(admin.TabularInline):
    model = Experience
    readonly_fields = ('id',)
    extra = 1


class ResumeotherSkillInline(admin.TabularInline):
    model = otherSkill
    readonly_fields = ('id',)
    extra = 1


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['university', 'update_at', 'status']
    inlines = [ResumeSkillInline, ResumeEducationInline, ResumeotherSkillInline, ResumeExperienceInline]



class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'update_at']
    list_filter = ['update_at']


admin.site.register(Setting, SettingAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Blog, BlogAdmin)
