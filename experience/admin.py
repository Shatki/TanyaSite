from django.contrib import admin
from .models import Course, Award


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'place',
                    'begin_date',
                    'finish_date',
                    'duration',
                    )

    search_fields = ('name', 'place')
    ordering = ('name', 'place')
    list_filter = ('begin_date', 'finish_date')


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'date',
                    'description',
                    )

    search_fields = ('name', 'date',)
    ordering = ('name', 'date',)
    list_filter = ('date',)
