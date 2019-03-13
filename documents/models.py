from django.db import models
from users.models import User
from Tatyana.settings import DOCUMENTS_PDF_DIR, DOCUMENTS_MINIATURES_DIR, MEDIA_URL
from website.models import Menu


# Create your models here.
class Document(models.Model):
    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'
        db_table = 'documents'

    # комментатор
    author = models.ForeignKey(User, verbose_name=u'Кто добавил/автор документа', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name=u'Наименование документа',
                             unique=True, blank=False, null=False)
    description = models.CharField(max_length=200, verbose_name=u'описание документа',
                                   unique=True, blank=True, null=True)
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    allowed = models.BooleanField(verbose_name=u'разрешение на публикацию', default=False)
    doc = models.FileField(upload_to=DOCUMENTS_PDF_DIR, verbose_name=u'документ')
    miniature = models.ImageField(upload_to=DOCUMENTS_MINIATURES_DIR, verbose_name=u'миниатюра документа',
                                  name='preview', blank=True, default=DOCUMENTS_PDF_DIR + "pdf.png")
    page = models.ForeignKey(Menu, verbose_name=u'размещение документа',
                             on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return '%s %s' % (self.added, self.author)

    def preview(self):
        # return '%s/' % self.directory  # ВРЕМЕННО
        return self.miniature
