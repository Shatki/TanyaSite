# Generated by Django 2.1.7 on 2019-02-28 21:29

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20190228_2027'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='photo',
            managers=[
                ('label', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='label', to='gallery.Photo', verbose_name='Фотография профиля'),
        ),
    ]