import re
import os
from write_in_excel import write_in_excel as wr


def find_vs():
    # 当前路径
    path = os.getcwd()
    # 定义返回值
    dict_list = []

    # 打开日志
    with open(r'{}\waf-a.log'.format(path), 'r', encoding='GB18030') as f:
        # 编码方式根据文本类型不同选择UTF-8或者GB18030等等，可以通过notepad对文件进行重编码
        # 筛选vs
        config_str = f.read()
        vs = re.findall(r'ltm virtual (\S+) {', config_str)

        # 按照ltm配置文件规律，所有vs的都以ltm virtual <vs_name>开头
        # 日志配置security-log-profiles在中间
        # 然后是source 0.0.0.0/0的源地址配置
        #
        # 截取每个vs开始到source 0.0.0.0/0中间的配置
        vs_midconfig = []
        for i in vs:
            midconfig = re.findall(r'\s+ltm virtual\s+' + i + r'\s+{(?:.*\n)+' + '?\s+source 0.0.0.0/0', config_str)
            vs_midconfig.append(midconfig)

        # 在每个中段配置中检查log profile的配置情况

        # for x, y in zip(vs, vs_midconfig):
        for i in range(len(vs)):
            vs_name = vs[i]
            if re.findall('remote_log', str(vs_midconfig[i])):
                remote_log = 1
            else:
                remote_log = 0
            if re.findall('Log illegal requests', str(vs_midconfig[i])):
                illegal_request = 1
            else:
                illegal_request = 0
            # 将结果压入字典
            d = {'vs_name': vs_name, 'remote_log': remote_log, 'illegal_request': illegal_request}
            dict_list.append(d)
    return dict_list


if __name__ == '__main__':

    filename = 'f5_remote_logs.xlsx'
    title = ['vs_name', 'remote_log', 'illegal_request']
    data = find_vs()
    wr(filename, title, data)
