from django.db import models
from django.urls import path


class TableField(models.Model):
    model_id = models.IntegerField(primary_key=True, verbose_name='Порядковый номер')
    name = models.CharField(max_length=64, verbose_name='Имя')
    width = models.IntegerField(verbose_name='Ширина')


class CsvPath(models.Model):
    csvPath = models.CharField(max_length=200, verbose_name='Путь к файлу')

    class Meta:
        verbose_name = 'Путь к файлу'
        verbose_name_plural = 'Пути к файлам'

    def get_path(self):
        return self.csvPath

    def set_path(self, new_path):
        self.csvPath = new_path
        self.save()

    def save(self, *args, **kwargs):
        obj = CsvPath.objects.all()
        if obj.count() == 0 or self.pk == 1:
            super(CsvPath, self).save(*args, **kwargs)

    def __str__(self):
        return path.basename(self.csvPath)
