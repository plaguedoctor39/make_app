from django.db import models


class TableField(models.Model):
    model_id = models.IntegerField(primary_key=True, verbose_name='Порядковый номер')
    name = models.CharField(max_length=64, verbose_name='Имя')
    width = models.IntegerField(verbose_name='Ширина')


class SavePath(models.Model):
    file_path = models.FilePathField(path='/Users/daniil/PycharmProjects/make_app/', match='#*\.csv$',
                                     recursive=True, verbose_name='Путь к файлу')

    def set_path(self, path):
        SavePath.save(path)

    def get_path(self):
        return self.file_path
