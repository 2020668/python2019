import xlrd
import pymysql


# import importlib
# importlib.reload(sys) #出现呢reload错误使用


def open_excel():
    try:
        book = xlrd.open_workbook("Schedule of Receiving Team.xlsx")  # 文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("sheet名称")  # execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")