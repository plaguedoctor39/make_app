# Generated by Django 2.2.10 on 2020-08-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0008_auto_20200829_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savepath',
            name='file_path',
            field=models.FilePathField(match='#*\\.csv$', path='/Users/daniil/PycharmProjects/make_app/', recursive=True, verbose_name='Путь к файлу'),
        ),
    ]
