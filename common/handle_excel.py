import os

import openpyxl
from  common.handle_path import DATA_DIR

class HandleExcel():
    def __init__(self,file_name,sheet_name):
        self.filename=file_name
        self.sheetname=sheet_name

    def read_data(self):
        workbok=openpyxl.load_workbook(self.filename)
        sn=workbok[self.sheetname]

        res=list(sn.rows)

        title= [i.value for i in res[0]]

        cases=[]
        for item in res[1:]:
            data=[case.value for case in item]
            dic=dict(zip(title,data))
            cases.append(dic)
        return cases

    def write_date(self):
        pass
# if __name__ == '__main__':
#     hd=HandleExcel(os.path.join(DATA_DIR,"cases.xlsx"),"login")
#     cases=hd.read_data()
#     print(cases)



