# Generated by Django 2.1.7 on 2019-03-03 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190303_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author',
        ),
    ]
