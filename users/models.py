from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from Tatyana.validators import alpha_all, login, email
from Tatyana.settings import PROFILE_PHOTOS_DIR, PROFILE_PHOTO_DEFAULT_NAME


# Класс менеджера должен переопределить методы create_user() и create_superuser().
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        db_table = 'users'

    # Имя логина авторизации
    username = models.CharField(verbose_name=u'имя пользователя в системе', unique=True, max_length=30, db_index=True,
                                validators=[login])
    # Авторизация будет происходить по E-mail
    email = models.EmailField(verbose_name=u'электронная почта', unique=True, max_length=255, validators=[email])
    # Имя - не является обязательным
    first_name = models.CharField(verbose_name=u'имя пользователя', max_length=40, blank=True, null=True)
    # Фамилия - также не обязательна
    last_name = models.CharField(verbose_name=u'фамилия пользователя', max_length=40, blank=True, null=True)

    photo = models.ImageField(upload_to=PROFILE_PHOTOS_DIR, verbose_name=u'фото', blank=True, null=True,
                              default=PROFILE_PHOTO_DEFAULT_NAME)
    # Атрибут суперпользователя
    is_admin = models.BooleanField(default=False, null=False)

    date_joined = models.DateTimeField(verbose_name=u'дата создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=u'последнее обновление', auto_now=True)
    objects = UserManager()

    # логинимся
    USERNAME_FIELD = 'email'
    # обязательное поле
    REQUIRED_FIELDS = ['username', ]

    def __unicode__(self):
        return '%d: %s' % (self.id, self.username)

    def __str__(self):
        return self.username

    def get_photo(self):
        return self.photo

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Отправляет электронное письмо этому пользователю.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def has_perm(self, perm, obj=None):
        return True
