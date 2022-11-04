import openpyxl
class Excel:
    def get_cellValue(path,sheet,row,col):
        workBook = openpyxl.load_workbook(path)
        value = workBook[sheet].cell(row,col).value
        print("xl cell value is : ",value)
        return value