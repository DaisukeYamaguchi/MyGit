# -*- coding: utf-8 -*-

def read_xls(file):
    import xlrd
    book = xlrd.open_workbook(file)
    names = book.sheet_names()
    data = []
    for i in range(len(names)):
        sheet = book.sheet_by_index(i)
        for row in range(sheet.nrows):
            for col in range(sheet.ncols):
                data.append([file, names[i], row, col, sheet.cell(row, col).value])
    return data


