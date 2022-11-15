from xlrd import open_workbook
import json


def excel_to_json(input):
    workbook = open_workbook(input,"r")

    header_list=['Quote Number','Date','Ship To','Ship From','Name']
    item_column = ['LineNumber','PartNumber','Description','Price']
    sheet = workbook.sheet_by_index(0)
    values = []
    cellObj = {'item':[]}
    first_row = []
    data = {}
    start_item_column_row_index = -1
    start_col_index_arr = []  
    for header_value in header_list:
        for row_idx in range(1, sheet.nrows):
            for col_idx in range(1, sheet.ncols):
                if header_value == str(sheet.cell(row_idx, col_idx).value):
                    cellObj[header_value] = str(sheet.cell(row_idx, col_idx+1).value)
                if str(sheet.cell(row_idx, col_idx).value)=='-----------':
                    break
            
    for row_idx in range(1, sheet.nrows):
        for col_idx in range(1, sheet.ncols):
            for item in item_column:
                if item == str(sheet.cell(row_idx, col_idx).value):
                        start_item_column_row_index = row_idx
                        start_col_index_arr.append(col_idx)
                        data[item]=[]


        if  start_item_column_row_index!=-1 and start_item_column_row_index!=row_idx: 
            for arr_index,item1 in zip(start_col_index_arr,data):
                if str(sheet.cell(row_idx, arr_index).value)!='':
                    data[item1].append(str(sheet.cell(row_idx, arr_index).value))
        if str(sheet.cell(row_idx, col_idx).value)=='-----------':
            break
    item_length = len(item_column)
    length_dict = len(data['LineNumber'])
    i=0
    j=1

    for index in range(0,length_dict):
        cellObj['item'].append(index)
        for keys in item_column:
            
            if type(cellObj['item'][index]) is not dict:
                cellObj['item'][index]={keys:data[keys][index]}
            else:
                cellObj['item'][index].update({keys:data[keys][index]})
    return cellObj;        



cellObj= excel_to_json("Python_Skill_Test.xlsx")


print(cellObj)



