from django.db import models
from .constants import MENU_CHOICES, MENU_DEFAULT


# Create your models here.
class Menu(models.Model):
    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'пункты меню'
        db_table = 'menus'

    name = models.CharField(max_length=50, verbose_name='наименование пункта меню')
    menu = models.CharField(verbose_name=u"корневое меню", default=MENU_DEFAULT,
                            max_length=20, blank=False, choices=MENU_CHOICES)
    url = models.CharField(max_length=200, verbose_name=u"гиперссылка на страницу")

    def __str__(self):
        return self.name

    def get_type(self):
        return self.menu

    def get_file(self):
        return self.url
