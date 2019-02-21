import xlrd, openpyxl

# workbook = xlrd.open_workbook('//home//lisir//文档//HC//新系统使用人员名单.xls')
# print(workbook.sheet_names())  # 查看所有sheet
# booksheet = workbook.sheet_by_index(0)  # 用索引取第一个sheet
# booksheet = workbook.sheet_by_name('Sheet 1')  # 或用名称取sheet
# # 读单元格数据
# cell_11 = booksheet.cell_value(0, 0)
# cell_21 = booksheet.cell_value(1, 0)
# # 读一行数据
# row_3 = booksheet.row_values(2)
# print(cell_11, cell_21, row_3)

workbook = openpyxl.load_workbook('//home//lisir//文档//HC//新系统使用人员名单.xlsx')
# booksheet = workbook.active                #获取当前活跃的sheet,默认是第一个sheet
sheets = workbook.get_sheet_names()  # 从名称获取sheet
booksheet = workbook.get_sheet_by_name(sheets[0])
print(booksheet)
name = booksheet.title
print("name:", name)
#获取该表相应的行数和列数
rows = booksheet.rows
rows2 = booksheet.max_row
print(rows)
print(rows2)
columns = booksheet.columns
columns2 = booksheet.max_column
print(columns)
print(columns2)

user = dict()
roles = None
# 迭代所有的行sheet.rows，这是一个生成器，里面是每一行数据，每一行数据由一个元组类型包裹。
for row in rows:
    line = [col.value for col in row]
    if not isinstance(line[4], int):
        continue

    user['username'] = line[3]
    user['name'] = line[2]
    user['password'] = line[4]
    user['check_password'] = line[4]
    user['group'] = "制衣技术"
    if line[1]:
        roles = line[1]
        user['roles'] = roles
    else:
        user['roles'] = roles
    print(user)

# 通过坐标读取值
# cell_11 = booksheet.cell('A1').value..
# cell_11 = booksheet.cell(row=1, column=1).value
print(5555555555555555555555555555555555555555555555555555555555555555)


