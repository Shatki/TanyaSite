# Generated by Django 2.1.7 on 2019-02-28 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20190228_2129'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='photo',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='label',
        ),
        migrations.AddField(
            model_name='photo',
            name='label',
            field=models.BooleanField(default=False, verbose_name='сделать фотографией профиля'),
        ),
    ]