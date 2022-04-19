import re
import os




def get_sn(str1):
    # 获取exe当前所在路径:
    path = (os.getcwd())

    # 在当前路径新建一个txt文件，将获取的sn写入txt
    with open('{}\{}_sn.txt'.format(path, ip), 'w', encoding='utf-8') as f2:
        # slot cpu sn
        slot = re.findall('(Slot\s+\d+\s+CPU\s+\d+):\s+\w+\s+:\s+\S+\s+DEVICE_(SERIAL_NUMBER\s+:\s+\S+)', str1)
        for i in range(len(slot)):
            print(slot[i][0], file=f2)
            print(slot[i][1], file=f2)
        # fan sn
        fan = re.findall('(FAN\s+\d+\s):\s+\w+\s+:\s+\S+\s+DEVICE_(SERIAL_NUMBER\s+:\s+\S+)', str1)
        for i in range(len(fan)):
            print(fan[i][0], file=f2)
            print(fan[i][1], file=f2)

        # 接口sn
        interface = re.findall(
            '(\w+-?Gig\S+)\s+transceiver\s+manufacture\s+information:\s+Manu. (Serial Number :\s+\w+)',
            str1)

        for i in range(len(interface)):
            print(interface[i][0], file=f2)
            print(interface[i][1], file=f2)
