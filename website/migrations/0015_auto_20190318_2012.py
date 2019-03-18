# Generated by Django 2.1.7 on 2019-03-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_feedback_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'сообщение с формы обратной связи', 'verbose_name_plural': 'сообщения с формы обратной связи'},
        ),
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(default=1, max_length=50, verbose_name='полное наименование страницы меню(отображается в заголовках)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, verbose_name='наименование страницы меню(отображается в навигации)'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='page',
            field=models.CharField(choices=[('null_page', 'Страница еще не создана'), ('special', 'Специализированная страница без выбора типа контента'), ('documents', 'Страница с документами'), ('editor', 'Страница с редактированием текста')], default='null_page', max_length=20, verbose_name='тип страницы'),
        ),
    ]
