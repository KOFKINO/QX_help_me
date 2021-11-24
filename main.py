import re
import os
import paramiko

# ip = input('请输入设备ip：')
# username = input('请输入用户名：')
# pswd = input('请输入密码：')

ip = '172.17.1.3'
username = 'admin'
pswd = 'H3c.com!123'


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


# ssh登录
def ssh_denglu(sship, sshusername, sshpassword, sshport=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sship, port=sshport, username=sshusername, password=sshpassword, timeout=5, compress=True)


# ssh执行命令
def ssh_command(cmd=''):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    stdin, stdout, stderr = ssh.exec_command(cmd)
    xx = stdout.read().decode()
    return xx


if __name__ == '__main__':
    ssh_denglu(ip, username, pswd)
    ssh_command('screen-length disable')
    x = ssh_command('display device manuinfo')
    get_sn(x)
