from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    inflation = []
    with open('inflation_russia.csv') as csvfile:
        inflation_reader = csv.reader(csvfile)
        for row in inflation_reader:
            inflation.append(row[0].split(';'))
        header = inflation[0]
        # print(inflation)
        inflation.pop(0)
        new_inflation = []
        new_row = []
        for row in inflation:
            for el in row:
                if len(new_row) == 0:
                    new_row.append(int(el))
                    continue
                if len(new_row) == 13:
                    new_row.append(el)
                    continue
                if el == '':
                    new_row.append(el)
                    continue
                else:
                    new_row.append(float(el))
            # print(new_row)
            new_inflation.append(new_row)
            new_row = []
        # print(new_inflation)

    context = {'table': new_inflation,
               'head': header}

    return render(request, template_name,
                  context)