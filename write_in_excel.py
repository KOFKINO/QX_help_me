import openpyxl as op


# 传入文件名（带后缀），列表标题， 和数据， 生产excel文件
# filename为字符串 # title为列表  # date 为字典组成的列表

def write_in_excel(filename, title, data):
    wb = op.Workbook()
    ws = wb['Sheet']
    # 添加表头
    ws.append(title)

    # 写入数据
    for i in data:  # 取出一个字典，其中的value即为一行数据
        # 创建一个列表，将字典的value存储到列表中
        key_list = []
        value_list = []
        for key, value in i.items():
            key_list.append(key)
            value_list.append(value)

        # 是否写入key值酌情使用，通常不需要！！
        # 按该行数据写入表格
        ws.append(value_list)

    # 保存文档
    wb.save(filename)


if __name__ == '__main__':
    f = 'test.xlsx'
    t = ['标题1', 'title2', 'title3']
    d = [{'k': 'k1', 'k2': 'k2', 'k3': 'k3'}, {'k': 'k4', 'k2': 'k5', 'k3': 'k6'}, {'k': '1', 'k2': 'k2'}]
    write_in_excel(f, t, d)
