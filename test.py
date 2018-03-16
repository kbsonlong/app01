# -*- coding: utf-8 -*-
import paramiko

def ssh_command(ip, user, passwd, command, port=22):
    pkey = 'app01/vps'  # 本地密钥文件路径[此文件服务器上~/.ssh/id_rsa可下载到本地]
    key = paramiko.RSAKey.from_private_key_file(pkey,password='')  # 有解密密码时,
    paramiko.util.log_to_file('paramiko.log')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 通过公共方式进行认证 (不需要在known_hosts 文件中存在)
    # ssh.load_system_host_keys() #如通过known_hosts 方式进行认证可以用这个,如果known_hosts 文件未定义还需要定义 known_hosts
    ssh.connect(ip, username=user, password=passwd,port=port, pkey=key)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = ''
    if stdout:
        result = stdout.read()
    elif stderr:
        result = stderr.read()

    print result
    return result




ssh_command('172.96.247.193', 'root', '', 'ps -ef', 22)