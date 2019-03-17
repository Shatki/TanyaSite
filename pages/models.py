from django.db import models
from users.models import User
from Tatyana.settings import DOCUMENTS_PDF_DIR, DOCUMENTS_MINIATURES_DIR, DOCUMENT_TYPES
from Tatyana.settings import PPTX, PDF, PPT, XLS, XLSX, DOC, DOCX, UNKNOWN
from website.models import Menu
from ckeditor.fields import RichTextField


# Create your models here.
class Document(models.Model):
    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'
        db_table = 'documents'

    # комментатор
    title = models.CharField(max_length=100, verbose_name=u'Наименование документа',
                             unique=True, blank=False, null=False)
    description = models.CharField(max_length=200, verbose_name=u'описание документа',
                                   unique=True, blank=True, null=True)
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=u'Кто добавил/автор документа', on_delete=models.CASCADE)

    doc = models.FileField(upload_to=DOCUMENTS_PDF_DIR, verbose_name=u'документ')

    preview = models.ImageField(upload_to=DOCUMENTS_MINIATURES_DIR, verbose_name=u'миниатюра документа',
                                blank=True, default=None)
    page = models.ForeignKey(Menu, verbose_name=u'размещение документа',
                             on_delete=models.CASCADE, blank=False, null=False)
    allowed = models.BooleanField(verbose_name=u'разрешение на публикацию', default=False)
    type = models.CharField(max_length=7, verbose_name='тип документа', choices=DOCUMENT_TYPES, default=PDF)

    def __str__(self):
        return '%s %s' % (self.added, self.author)

    def save(self, *args, **kwargs):
        # print(self.doc.url[-4:])
        if self.doc.url[-3:].lower() == PDF:
            self.type = PDF
        elif self.doc.url[-3:].lower() == PPT:
            self.type = PPT
        elif self.doc.url[-3:].lower() == DOC:
            self.type = DOC
        elif self.doc.url[-3:].lower() == XLS:
            self.type = XLS
        elif self.doc.url[-4:] == PPTX:
            self.type = PPTX
        elif self.doc.url[-4:].lower() == DOCX:
            self.type = DOCX
        elif self.doc.url[-4:].lower() == XLSX:
            self.type = XLSX
        else:
            self.type = UNKNOWN
        # Photo.objects.filter(album=self.album, label=True).update(label=False)
        # print('type:' + self.doc.url[-3:])
        super(Document, self).save(*args, **kwargs)


class Editor(models.Model):
    class Meta:
        verbose_name = 'текстовая страница'
        verbose_name_plural = 'текстовые страницы'
        db_table = 'editors'

    title = models.CharField(max_length=100, verbose_name=u'Наименование текста',
                             unique=True, blank=False, null=False)
    description = models.CharField(max_length=200, verbose_name=u'описание содержания',
                                   unique=True, blank=True, null=True)
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=u'Кто добавил/автор текста', on_delete=models.CASCADE)

    text = RichTextField(verbose_name=u'редактированный текст')

    page = models.ForeignKey(Menu, verbose_name=u'размещение документа',
                             on_delete=models.CASCADE, blank=False, null=False)
    allowed = models.BooleanField(verbose_name=u'разрешение на публикацию', default=False)

    def __str__(self):
        return '%s %s' % (self.title, self.description)
