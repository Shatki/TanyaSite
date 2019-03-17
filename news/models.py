from datetime import datetime
from django.db import models
from Tatyana.settings import NEWS_PHOTOS_DIR, PROFILE_PHOTOS_DIR, NEWS
from users.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class News(models.Model):
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        db_table = 'news'

    title = models.CharField(max_length=50, verbose_name=u'заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    updated = models.DateTimeField(verbose_name=u'последнее обновление', auto_now=True)
    photo = models.ImageField(upload_to=NEWS_PHOTOS_DIR, verbose_name=u'фотография', name='photo', blank=False)
    # пока не будем делать
    # tags = models.ManyToManyField(Tags,verbose_name=u'теги')

    fix = models.BooleanField(u'закрепить новость как основную', default=False, blank=True)
    text = RichTextField(verbose_name=u'текст новости')

    def save(self, *args, **kwargs):
        News.objects.all().update(fix=False)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def url(self):
        return '%s/%s/' % (NEWS, self.id)

    def date(self):
        return '{:0>2}/{:0>2}/{:0>2}'.format(str(self.added.day), str(self.added.month), str(self.added.year))


class Comment(models.Model):
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        db_table = 'comments'

    # комментатор
    author = models.CharField(max_length=50, verbose_name=u'имя комментатора')
    email = models.EmailField(verbose_name=u'электронная почта')
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    allowed = models.BooleanField(verbose_name=u'разрешение на публикацию', default=False)
    news = models.ForeignKey(News, verbose_name=u'комментируемая новость', on_delete=models.CASCADE,
                             blank=False, null=False)
    reply = models.ForeignKey('self', verbose_name=u'ответ на комментарий', on_delete=models.CASCADE,
                              blank=True, null=True)
    message = RichTextField(verbose_name=u'текст комментария', blank=False, null=False)
    photo = models.ImageField(upload_to=PROFILE_PHOTOS_DIR, verbose_name=u'фотография профиля',
                              name='photo', blank=True)

    def __str__(self):
        return '%s %s' % (self.added, self.author)
