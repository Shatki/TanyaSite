from django.db import models
from Tatyana.settings import GALLERY_PHOTOS_DIR


class Photo(models.Model):
    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
        db_table = 'photos'

    name = models.CharField(max_length=50, verbose_name='наименование', null=False)
    description = models.CharField(max_length=50, verbose_name='описание', null=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, null=False,
                              verbose_name=u'принадлежность к альбому')
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    updated = models.DateTimeField(verbose_name=u'последнее обновление', auto_now=True)
    photo = models.ImageField(upload_to=GALLERY_PHOTOS_DIR, verbose_name=u'фотография', name='photo')

    label = models.BooleanField(u'сделать фотографией профиля', default=False)

    def save(self, *args, **kwargs):
        Photo.objects.filter(album=self.album, label=True).update(label=False)
        super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def dir(self):
        return self.album

    def get_photo(self):
        return self.photo


class Album(models.Model):
    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'
        db_table = 'albums'

    name = models.CharField(max_length=50, verbose_name='наименование альбома(рус)', unique=True)
    description = models.CharField(max_length=50, verbose_name='описание альбома(не обязательно)', null=True, blank=True)
    directory = models.CharField(max_length=200, verbose_name=u"псевдоним альбома(англ)", unique=True)

    def __str__(self):
        return self.directory

    def url(self):
        # return '%s/' % self.directory  # ВРЕМЕННО
        return '/%s%s/' % (GALLERY_PHOTOS_DIR, self.directory)  # ВРЕМЕННО
