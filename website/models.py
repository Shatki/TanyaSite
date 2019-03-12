from django.db import models
from Tatyana.settings import MENU_CHOICES, MENU_DEFAULT


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


class Section(models.Model):
    class Meta:
        verbose_name = "секция"
        verbose_name_plural = 'секции'
        db_table = 'sections'
    name = models.CharField(verbose_name=u'наименование секции', max_length=30, unique=True, db_index=True)
    # section_id = models.CharField(verbose_name=u'id секции', max_length=30, unique=True, db_index=True)
    # section_content = RichTextField(verbose_name=u'HTML контент', max_length=5000)
    enable = models.BooleanField(verbose_name=u'активность секции')

    def __str__(self):
        return self.name
