from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


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
