from django.contrib import admin
from table.models import *


@admin.register(TableField)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(CsvPath)
class FileAdmin(admin.ModelAdmin):
    pass
