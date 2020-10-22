import xlrd
from collections import OrderedDict
from collections import namedtuple
import prettytable


class ExcelTemplate:

    def __init__(self, excel_file, sheet_name):
        self.excel_file = excel_file
        self.sheet_name = sheet_name
        self.template_book = xlrd.open_workbook(self.excel_file)
        self.template_sheet = self.template_book.sheet_by_name(self.sheet_name)
        self.number_of_rows = self.template_sheet.nrows
        self.number_of_cols = self.template_sheet.ncols

    def unique_value_dict(self, title_value):
        unique_values = set()
        unique_dict = OrderedDict()
        a = 0
        for unique in range(1, self.number_of_rows):
            unique_values.add(self.template_sheet.cell(unique, title_value).value)
        for unique_value in unique_values:
            unique_dict[a] = unique_value
            a += 1
        return unique_dict

    def Title_row_dict(self):
        # show all available Titles
        title_dict = OrderedDict()
        y = 0
        for x in range(self.number_of_cols):
            title_dict[y] = self.template_sheet.cell(0, y).value
            y += 1
        return title_dict

    def xl_filter(self):
        device_list = []
        title_row_dict = self.Title_row_dict()
        for x in title_row_dict.items():
            print(x)
        title_row_selected = int(input("Select a Value: "))
        unique_value_dict = self.unique_value_dict(title_row_selected)
        for y in unique_value_dict.items():
            print(y)
        value_selected = int(input("Select a Value: "))
        dict_value = unique_value_dict[value_selected]

        for i in range(self.number_of_rows):
            if self.template_sheet.cell(i, title_row_selected).value == dict_value:
                device_loc = self.template_sheet.cell(i, 0).value
                serial_num = self.template_sheet.cell(i, 1).value
                device_nam = self.template_sheet.cell(i, 2).value
                device_typ = self.template_sheet.cell(i, 3).value
                device_ipd = self.template_sheet.cell(i, 4).value
                device_sov = self.template_sheet.cell(i, 5).value
                device_mod = self.template_sheet.cell(i, 6).value
                device_acc = self.template_sheet.cell(i, 7).value
                device_list.append([device_loc, serial_num, device_nam, device_typ,
                                    device_ipd, device_sov, device_mod, device_acc])
        return device_list


file1 = ExcelTemplate("MyDevicesUploadTemplate.xls", "MyDevicesUploadTemplate")
readable_table = prettytable.PrettyTable(file1.Title_row_dict().values())
filtered_list = file1.xl_filter()
for x in filtered_list:
    readable_table.add_row(x)
print(readable_table)

