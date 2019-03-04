from django.contrib import admin
from .models import News, Comment


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'added',
                    )

    search_fields = ('title',)
    ordering = ('added',
                'title'
                )


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author',
                    'allowed',
                    'added',
                    'news',
                    'reply'
                    )

    search_fields = ('news', 'added')
    ordering = ('news', 'added')
    list_filter = ('news', 'added')
