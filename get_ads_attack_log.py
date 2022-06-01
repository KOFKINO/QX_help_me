import re
import os
import openpyxl as op


def find_attack_log(file):

    # 定义返回值
    dict_list = []

    # 打开日志
    with open(file, 'r', encoding='UTF-8') as f:
        # 编码方式根据文本类型不同选择UTF-8或者GB18030等等，可以通过notepad对文件进行重编码
        # 筛选时间
        log = f.read()
        # 获取时间戳和每个时间戳下面的分段日志
        # 格式为
        # 日期
        # 攻击日志
        # 日期
        # 攻击日志
        # ...
        # 所以第一个分割出来的攻击日志为空''
        # 第n个日期对应的实际上是第n+1个攻击日志，所以需要弹出第一个空攻击日志完成一一对应
        time_fragment = re.findall(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\s+', log)
        # print(time_fragment)
        log_fragment = re.split(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\s+', log)
        log_fragment.pop(0)
        # print(log_fragment[0])

        # # 打开excel
        # wb = op.Workbook()
        # ws = wb['Sheet']

        # 已有表格，追加数据
        wb = op.load_workbook('ads.xlsx')
        ws = wb['Sheet1']

        # 在每段日期和日志中检索跟目的ip有关的日志,并写入
        for i in range(len(time_fragment)):
            line = log_fragment[i].split('\n')
            for x in range(len(line)):
                l1 = []
                if '39.155.175.223' in line[x]:
                    l1.append(time_fragment[i])
                    l1.append(line[x])
                    ws.append(l1)
                if '39.155.175.233' in line[x]:
                    l1.append(time_fragment[i])
                    l1.append(line[x])
                    ws.append(l1)
                if '39.155.175.238' in line[x]:
                    l1.append(time_fragment[i])
                    l1.append(line[x])
                    ws.append(l1)
        wb.save('ads.xlsx')


def get_log_file():
    # 当前路径
    path = os.getcwd()
    file_list= []
    for x in os.listdir():
        if re.search('.log$', x):
            file_list.append(x)
    return file_list


if __name__ == '__main__':
    log = get_log_file()
    for i in log:
        find_attack_log(i)