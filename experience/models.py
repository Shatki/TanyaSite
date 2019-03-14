"""
    Функциональные блоки сайта

"""
from Tatyana.settings import CONTENT_PIC_DEFAULT_NAME, CONTENT_PICS_DIR, AWARDS_PHOTOS_DIR, AWARDS_CHOICES
from django.db import models
from ckeditor.fields import RichTextField


class Content(models.Model):
    class Meta:
        verbose_name = 'загружаемый контент'
        verbose_name_plural = 'загружаемый контент'
        db_table = 'content'

    TEXT = 'text'
    PIC = 'pic'
    VIDEO = 'VIDEO'
    DOC = 'doc'

    CONTENT_CHOICES = (
        (TEXT, 'Текст'),
        (PIC, 'Изображение'),
        (VIDEO, 'Видео'),
        (DOC, 'Документ'),

    )

    name = models.CharField(max_length=30, verbose_name='наименование контента')
    type = models.CharField(verbose_name=u"тип контента", default=PIC,
                            max_length=20, blank=False, choices=CONTENT_CHOICES)
    file = models.ImageField(upload_to=CONTENT_PICS_DIR, verbose_name=u'изображение', blank=True, null=True,
                             default=CONTENT_PIC_DEFAULT_NAME)
    text = RichTextField(verbose_name=u"блок текста")

    def __str__(self):
        return self.name

    def get_type(self):
        return self.type

    def get_file(self):
        return self.file


class Course(models.Model):
    class Meta:
        verbose_name = 'курс повышения квалификации'
        verbose_name_plural = 'курсы повышения квалификации'
        db_table = 'courses'

    name = models.CharField(max_length=100, verbose_name='название курса повышения квалификации', blank=False, null=False)
    begin_date = models.DateField(verbose_name='дата начала курса', blank=False, null=False)
    finish_date = models.DateField(verbose_name='дата завершения курса', blank=False, null=False)
    duration = models.IntegerField(verbose_name='длительность курса(часов)', blank=True, null=True)
    place = models.CharField(max_length=100, verbose_name='место проведения курса', blank=False, null=False)

    def __str__(self):
        return self.name

    def full(self):
        return "%s-%s, %s, %sч., %s" % (self.begin_date, self.finish_date, self.name, self.duration, self.place)


class Award(models.Model):
    class Meta:
        verbose_name = 'награда'
        verbose_name_plural = 'награды'
        db_table = 'awards'

    name = models.CharField(max_length=50, verbose_name='Описание', null=False)
    description = models.CharField(choices=AWARDS_CHOICES, max_length=50, verbose_name='Тип',
                                   default=1, null=False, blank=False)
    date = models.DateField(verbose_name='дата получения')
    photo = models.ImageField(upload_to=AWARDS_PHOTOS_DIR, verbose_name=u'изображение/скан')

    def __str__(self):
        return self.name
