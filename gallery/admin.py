from django.contrib import admin
from .models import Album, Photo


# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'directory',
                    )

    search_fields = ('name',)
    ordering = ('name', 'directory')

# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'description',
                    'album',
                    'added',
                    'updated',
                    )

    search_fields = ('name', 'added')
    ordering = ('name', 'album')
    list_filter = ('added', 'album')
