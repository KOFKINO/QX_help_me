import re
import os

def find_vs():
    # 当前路径
    path = os.getcwd()
    # 定义返回值
    dict_list = []

    # 打开日志
    with open(r'{}\ltm.txt'.format(path), 'r', encoding='UTF-8') as f:
        # 编码方式根据文本类型不同选择UTF-8或者GB18030等等，可以通过notepad对文件进行重编码
        # 筛选vs
        config_str = f.read()
        vs = re.findall(r'ltm virtual (\S+) {', config_str)


        # 按照ltm配置文件规律，所有vs的都以ltm virtual <vs_name>开头
        # 日志配置security-log-profiles在中间
        # 然后是source 0.0.0.0/0的源地址配置
        #
        # 截取每个vs开始到source 0.0.0.0/0中间的配置
        vs_ip = []
        for i in vs:
            midconfig = re.findall(r'\s+ltm virtual\s+' + i + r'\s+{(?:.*\n)+' + '?\s+destination\s+\S+', config_str)
            ip = re.findall('destination\s+(\d+.\d+.\d+.\d+)',str(midconfig))
            print(ip)
            vs_ip.append(ip)



if __name__ == '__main__':
    find_vs()