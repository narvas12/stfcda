from django.contrib import admin
from .models import Contact, Journal, Members, Todos


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_published']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'title', 'is_active', 'is_trustee', 'is_member']
    prepopulated_fields = {'slug': ('full_name',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']


@admin.register(Todos)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['title']
