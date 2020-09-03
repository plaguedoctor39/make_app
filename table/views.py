from django.shortcuts import render
import csv
from .models import *


def table_view(request):
    template = 'table.html'
    columns = TableField.objects.all()
    csv_filename = CsvPath.objects.first()
    with open(csv_filename.get_path(), 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': columns,
            'table': table,
            'csv_file': csv_filename.get_path()
        }
        result = render(request, template, context)
    return result