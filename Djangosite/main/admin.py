from django.contrib import admin
from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about', 'photo', 'active')
    list_display_links=('id', 'name')
    search_fields = ('name', 'about')

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','person', 'projName', 'desc', 'tech', 'comment', 'link','photo')
    list_display_links=('id', 'projName')
    search_fields = ('projName', 'desc')
    prepopulated_fields = {"slug": ("projName",)}

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id','person', 'backend', 'frontend', 'linux', 'windows', 'databases', 'virtualization', 'softskills',)
    list_display_links=('id', 'person')
    search_fields = ('id', 'person')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'company', 'post', 'info','dateStart','dateEnd')
    list_display_links=('id', 'company')
    search_fields = ('company', 'post')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'name', 'department', 'info', 'dateStart', 'dateEnd')
    list_display_links=('id', 'name')
    search_fields = ('name', 'department')

class MailNotificationAdmin(admin.ModelAdmin):
    list_display = ('id','person','mailPassword', 'isActive', 'mailLogin')
    list_display_links=('id', 'mailLogin')
    search_fields = ('id', 'mailLogin', 'isActive')

    def save_model(self, request, obj, form, change):
        encrypted_password = ""
        for char in obj.mailPassword:
            encrypted_password += chr(ord(char) + 6)
        obj.mailPassword = encrypted_password
        super().save_model(request, obj, form, change)

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'mail', 'github', 'telegram', 'location','policy')
    list_display_links=('id', 'mail', 'github', 'location', 'policy')
    search_fields = ('id', 'mail')

class Site_settingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'siteName', 'previewS', 'previewD', 'footerText')
    list_display_links=('id', 'siteName')
    search_fields = ('id', 'siteName')

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(MailNotification, MailNotificationAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Site_settings, Site_settingsAdmin)