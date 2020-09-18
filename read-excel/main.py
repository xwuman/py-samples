# coding=utf-8

import xlrd

def main():
	# 打开文件
	data = xlrd.open_workbook('demo.xlsx')

	# 查看工作表
	data.sheet_names()
	print("sheets：" + str(data.sheet_names()))

	# 通过文件名获得工作表,获取工作表1
	table = data.sheet_by_name('人员名单')

	# 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1
	# table = data.sheet_by_index(0)

	print("整行值：" + str(table.row_values(0)))
	print("整列值：" + str(table.col_values(1)))

	# 获取行数和列数
	# 行数：table.nrows
	# 列数：table.ncols
	print("总行数：" + str(table.nrows))
	print("总列数：" + str(table.ncols))

	for i in range(table.nrows):
		if i == 0:  # 第0行是标题
			continue
		id = str(table.cell(i, 0).value)
		name = str(table.cell(i, 1).value)
		sex = str(table.cell(i, 2).value)
		old = int(table.cell(i, 3).value)
		dept = str(table.cell(i, 4).value)
		tel = str(table.cell(i, 5).value)
		print("工号：%s, 姓名：%s, 年龄：%d, 部门：%s，电话：%s\r\n" %  (id, name, old, dept, tel))
	print("结束")
	
	
if __name__ == "__main__":
    main()