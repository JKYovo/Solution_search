import openpyxl

def move_data(src_sheet, dest_sheet, n):
    dest_row = 1
    for i in range(4 * n + 1, src_sheet.max_row + 1, 4):
        dest_sheet.cell(row=dest_row, column=1, value=src_sheet.cell(row=i, column=1).value)
        dest_sheet.cell(row=dest_row, column=2, value=src_sheet.cell(row=i, column=2).value)
        dest_sheet.cell(row=dest_row, column=3, value=src_sheet.cell(row=i+2, column=2).value)
        dest_sheet.cell(row=dest_row, column=4, value=src_sheet.cell(row=i+1, column=2).value)
        dest_sheet.cell(row=dest_row, column=5, value=src_sheet.cell(row=i, column=3).value)
        dest_row += 1

# 打开原始Excel文件
src_file_path = 'C:/Users/jky/Desktop/Excel(2).xlsx'
src_workbook = openpyxl.load_workbook(src_file_path)
src_sheet = src_workbook.active

# 创建新的Excel文件
dest_workbook = openpyxl.Workbook()
dest_sheet = dest_workbook.active

# 设置 n 值，根据规则进行数据移动
n = 0

# 调用函数进行数据移动
move_data(src_sheet, dest_sheet, n)

# 保存新的Excel文件
dest_file_path = 'C:/Users/jky/Desktop/new_data.xlsx'
dest_workbook.save(dest_file_path)

print("数据移动完成并存入新的Excel文件。")
