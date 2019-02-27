from django.contrib import admin
from .models import Menu


# Register your models here.

@admin.register(Menu)
class UserAdmin(admin.ModelAdmin):
    list_display = ('menu',
                    'name',
                    'url',
                    )

    search_fields = ('name',)
    ordering = ('menu',)
