# Generated by Django 2.1.7 on 2019-02-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, verbose_name='наименование пункта меню'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(max_length=200, verbose_name='гиперссылка на страницу'),
        ),
    ]
