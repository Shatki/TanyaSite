"""
    Функциональные блоки сайта

"""
from Tatyana.settings import CONTENT_PIC_DEFAULT_NAME, CONTENT_PICS_DIR
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





class Block(models.Model):
    class Meta:
        verbose_name = 'блок сайта'
        verbose_name_plural = 'блоки сайта'
        db_table = 'blocks'

    name = models.CharField(max_length=30, verbose_name='наименование блока')
    item = models.ManyToManyField(Content, verbose_name=u'изображение',
                                   #through='ContentTable',
                                   #through_fields=('content', 'item'),
                                   related_name='block_items'
                                   )
