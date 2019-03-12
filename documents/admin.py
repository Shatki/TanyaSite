from django.contrib import admin
from .models import Document


# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'author',
                    'description',
                    'allowed',
                    'added',
                    )

    search_fields = ('title', 'added')
    ordering = ('title', 'added')
    list_filter = ('title', 'added')
