from django.db import models
from Tatyana.settings import MENU_CHOICES, MENU_DEFAULT, TEMPLATE_DOCUMENTS, TEMPLATE_AWARDS, TEMPLATE_NO_PAGE
from Tatyana.settings import PAGE_TYPES, DOCS, EDITOR, SPECIAL, NULL_PAGE


# Create your models here.
class Menu(models.Model):
    class Meta:
        verbose_name = 'страница меню'
        verbose_name_plural = 'страницы меню'
        db_table = 'menus'

    name = models.CharField(max_length=50, verbose_name='наименование страницы меню(отображается в навигации)')
    title = models.CharField(max_length=50, verbose_name='полное наименование страницы меню(отображается в заголовках)')
    menu = models.CharField(verbose_name=u"корневое меню", default=MENU_DEFAULT,
                            max_length=20, blank=False, choices=MENU_CHOICES)
    url = models.CharField(max_length=200, verbose_name=u"гиперссылка на страницу")

    page = models.CharField(verbose_name='тип страницы', default=NULL_PAGE, choices=PAGE_TYPES, max_length=20, blank=False)

    def __str__(self):
        return self.name

    def get_type(self):
        return self.menu

    def get_url(self):
        if self.url[0] == "#":
            return "%s/%s" % (self.menu, self.url)
        return "%s/%s/" % (self.menu, self.url)


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


class Feedback(models.Model):
    class Meta:
        verbose_name = "сообщение с формы обратной связи"
        verbose_name_plural = 'сообщения с формы обратной связи'
        db_table = 'feedbacks'

    name = models.CharField(verbose_name=u'имя', max_length=100)
    email = models.CharField(verbose_name=u'email', max_length=50)
    subject = models.CharField(verbose_name=u'тема сообщения', max_length=100)
    message = models.CharField(verbose_name=u'текст сообщения', max_length=400)
    date = models.DateTimeField(verbose_name=u'время отправки', auto_now_add=True)

    def __str__(self):
        return "Автор:%s, тема сообщения:%s" % (self.name, self.subject)
