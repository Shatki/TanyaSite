from django.contrib import admin
from .models import Menu, Section, Feedback


# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu',
                    'name',
                    'page',
                    'url',
                    )

    search_fields = ('name',)
    ordering = ('menu',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    'subject',
                    'date',
                    'message',
                    )

    search_fields = ('name',)
    ordering = ('date',)



# Register your models here.
#@admin.register(Section)
#class SectionAdmin(admin.ModelAdmin):
#    fields = ('name',)
#    search_fields = ('name',)
#    list_display = ('name',)
