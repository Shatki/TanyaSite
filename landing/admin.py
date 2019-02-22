from django.contrib import admin
from django.contrib.admin import forms
from .models import Section


# Register your models here.
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    fields = ('name',)
    search_fields = ('name',)
    list_display = ('name',)


