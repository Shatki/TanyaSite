from django.contrib import admin
from .models import Menu
from .models import Section


# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu',
                    'name',
                    'url',
                    )

    search_fields = ('name',)
    ordering = ('menu',)


# Register your models here.
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    fields = ('name',)
    search_fields = ('name',)
    list_display = ('name',)
