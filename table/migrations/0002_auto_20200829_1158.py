# Generated by Django 2.2.10 on 2020-08-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savepath',
            name='file_path',
            field=models.FilePathField(path='/', verbose_name='Путь к файлу'),
        ),
    ]
