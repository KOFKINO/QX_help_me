import paramiko

ip = input('请输入设备ip：')
username = input('请输入用户名：')
pswd = input('请输入密码：')

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# ssh登录
def ssh(ip, username, password, port=22):
    ssh.connect()
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)


# ssh执行命令
def ssh_command(cmd=''):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

# # ssh函数测试
# if __name__ == '__main__':
#     print(ssh_command(ip, username, pswd))
#     # print(ssh_command('120.27.210.240', 'root', 'Echo3845185765', cmd='pwd'))
