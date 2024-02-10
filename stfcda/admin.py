from django.contrib import admin
from .models import Contact, Journal, Journalfiles, Members, Todos, Nomination, VolunteerApplication


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_published']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ['member', 'is_nominated', 'n_reason']



@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ['id','full_name', 'title', 'is_trustee', 'is_member', 'is_nominated']
    prepopulated_fields = {'slug': ('full_name',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']


@admin.register(Todos)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Journalfiles)
class JournalfilesAdmin(admin.ModelAdmin):
    list_display = ['title']
    
    
@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ['surname', 'position']