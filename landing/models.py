from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Paragraph(models.Model):
    name = models.CharField(verbose_name=u'параграф', max_length=30)


class Section(models.Model):
    name = models.CharField(verbose_name=u'наименование секции', max_length=30, unique=True, db_index=True)
    # section_id = models.CharField(verbose_name=u'id секции', max_length=30, unique=True, db_index=True)
    # section_content = RichTextField(verbose_name=u'HTML контент', max_length=5000)
    def __str__(self):
        return self.section_name
