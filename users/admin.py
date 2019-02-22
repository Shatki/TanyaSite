from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import forms

from .models import User


class UserCreationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )
        readonly_fields = (
            'date_joined',
            'date_updated',)


class UserChangeForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'is_admin',
            'user_permissions',
        )


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'last_login')

    list_filter = (
        'date_joined',
        'last_login',
    )
    readonly_fields = (
        'date_joined',
        'date_updated',
        'last_login',
    )

    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
            )
        }),

        (u'Персональная информация', {
            'fields': (
                'first_name',
                'last_name',
                'photo',
            )
        }),

        (u'Права доступа', {
            'fields': (
                'groups',
                'user_permissions',
                'is_admin',
            )
        }),

        (u'Важные даты', {
            'fields': (
                'last_login',
                'date_joined',
                'date_updated',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes':
                ('wide',),
            'fields': (
                'email',
                'password',
                'is_admin',
            )
        }),
    )

    search_fields = (
        'email',)

    ordering = (
        'date_joined',)

    filter_horizontal = (
        'groups',
        'user_permissions',
    )

# Register your models here.
